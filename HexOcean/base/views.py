from .forms import *
from django.http import  JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from HexOcean import settings
from .serializers import ImageSerializer,UserSerializer
from rest_framework import status
from PIL import Image as im
from datetime import datetime

# list all users /users/ url working for it
@api_view(['GET'])
def user_list(request):
    if request.method =="GET":
        users=User.objects.all()
        serializer = UserSerializer(users , many=True)
        return Response(serializer.data)

#it return user's images
@api_view(['GET'])
def image_list(request,pk):
    try:
        images= Image.objects.filter(owner=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":  
        serializer=ImageSerializer(images,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        
# if customer go to link it check if it expire or not
@api_view(['GET'])
def image_url(request,pk):
    image_name=f"static/images/{pk}"
    try:
        image=Image.objects.get(image=image_name)
    except:
       return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == "GET":  
        serializer = ImageSerializer(image) 
        time=serializer.data["created_time"]
        expire=serializer.data["expireTime"]
        if expire !=0:
            valid=check_expire(time,expire)
            if valid:
                return Response(serializer.data, status=status.HTTP_201_CREATED)    
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

#it upload image
@api_view(['POST'])
def uploadImage(request):
    response_dic={}
    data = request.data
    data.owner=request.POST.get('owner')
    user=User.objects.get(id=request.POST.get('owner'))
    tier=Tier.objects.get(id=user.tier.id)
    data.image = request.FILES.get('image')
    serializer = ImageSerializer(data=data)
    if serializer.is_valid(): 
        serializer.save()
        img_url=str(serializer.data['image'])
        if tier.access_original:
            response_dic["photo original link"]=img_url
    thumbnails=tier.thumbnails.all()
    for i in thumbnails:
        height=i.thumbnail
        url=f"{settings.MEDIA_ROOT}{img_url[7:]}"
        img = im.open(url)
        height_per = (height/float(img.size[1]))
        weight = int((float(img.size[0])*float(height_per)))
        img.thumbnail((weight,height))
        url_list=url.split('.')
        img_urls=url_list[0] + str(height)+"."+url_list[1]
        img.save(img_urls)
        link=split_link(img_url, height)
        response_dic[f"photo {height}x link"]=link
    return JsonResponse(response_dic)

#  i need this function to modify name of images after resizing
# it is not necessary but i designed to classify images 
def split_link(url,height):
    url_list=url.split('.')
    img_url=url_list[0] + str(height)+"."+url_list[1]
    return img_url

# i am doing because when i request created time it responding with string
def check_expire(time,expire):
    date_now=str(datetime.now().date())
    date_created=time[0:10]
    if date_now!=date_created:
        return False
    hour_now=datetime.now().hour
    hour_created=int(time[11:13])
    hour_dif=(hour_now-hour_created)*3600
    min_now=datetime.now().minute
    min_created=int(time[14:16])
    min_dif=(min_now-min_created)*60
    sec_now=datetime.now().second
    sec_created=int(time[17:19])
    sec_dif=sec_now-sec_created
    total_dif=hour_dif+min_dif+sec_dif
    if total_dif>expire:
        return False
    else:
        return True