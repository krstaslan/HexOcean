This project developed for HexOcean according to task definition.

Installation
1 - clone repo https://github.com/krstaslan/HexOcean
2 - create a virtual environment and activate
pip install virtualenv
virtualenv env
env\scripts\activate
3 - cd into project "cd Hexocean"
4 - pip install -r requirements.txt
5 - and then you need .env file because i hided my secret key or you can create your SECRET KEY.
  For generate Secret Key 
  Solution 1:
    python manage.py shell( will open python shell ) in shell write 
    "from django.core.management.utils import get_random_secret_key"  and
    "print(get_random_secret_key())" coppy generated secret key and go to settings.py and paste it like 
    SECRET_KEY = 'django-insecure-b(6po*cs%s%_@e%ssdasddrx854iersad_)c8asda='
  Solution 2:
    echo "SECRET_KEY=$(openssl rand -base64 32)" > .env  it will create .env file and write genreated secret key in to the file 
6 - python manage.py createsuperuser(create super user to access admin panel
7 - python manage.py makemigrations 
8 - python manage.py migrate
9 - python manage.py runserver




For the run this project quickly I didn't use Postgresql in here but i will upload my project again with Postgresql.![List all images user have](https://user-images.githubusercontent.com/63463164/174626754-47eb9b61-f192-442c-ac80-c2ab96c76b11.PNG)

in admin panel
![Admin  panel](https://user-images.githubusercontent.com/63463164/174625747-dc7df8fb-2a47-4ab2-a584-3043c2acfaa3.PNG)
and we can create new user
![create new user](https://user-images.githubusercontent.com/63463164/174626195-0246adf0-1763-42d3-946a-430879881fa5.PNG)
and for new user we can create new tier and we can add change ability to reach originial image and expire image.
![Create new tier](https://user-images.githubusercontent.com/63463164/174626372-f56495fd-7357-47de-99fd-090b3c2d51a9.PNG)

We can see al user accounts in this url
![list all users](https://user-images.githubusercontent.com/63463164/174626642-3a3760bf-79c6-4ffb-9095-1efb47f31bf2.PNG)

and for spesific user to list his/her all images we can use this url 
![List all images user have](https://user-images.githubusercontent.com/63463164/174626766-5306413c-fb94-48bd-9dc3-c21d4ff23743.PNG)

if user want to upload an image shuld define some values it depend on user plan 
1) if user in basic plan it will take only 200x thumnail of his/her picture
![Basic planed user](https://user-images.githubusercontent.com/63463164/174627030-de4d835a-8c97-4d3c-8f0c-6a3ae5403f90.PNG)

2) if user has premium tier, will take 200x and 400x thumnails of the pictures.
![premium planned user](https://user-images.githubusercontent.com/63463164/174627286-49ec3e11-5490-429d-a1f4-c8928fc4c837.PNG)

3) for user who have Enterprise plan will receive 3 link 200x and 400x thumnails of the pictures and the original link of the image 
![uploading image](https://user-images.githubusercontent.com/63463164/174627607-e485ea27-1482-4b7c-a650-8c20cdfa2aee.PNG)

Enterprise planed user can access to define expire image for that they should define the second between 300 and 30000 
if the link expired it will return status 404 
![expired image return status 404](https://user-images.githubusercontent.com/63463164/174628193-df58d233-8015-4041-958b-53d5059fc238.PNG)

if user try to uplad not jpeg or png format system will give error 
![just jpeg](https://user-images.githubusercontent.com/63463164/174628334-4f118b06-1af8-451e-8ba6-e9c0991d054f.PNG)

To list all images user have they should use this url and define their user id in url
![List all images user have](https://user-images.githubusercontent.com/63463164/174628444-c40f7954-0315-458f-8a22-4412d007d7bf.PNG)






