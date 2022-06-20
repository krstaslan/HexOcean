from django.test import TestCase
from .models import Image
# Create your tests here.
class ImageTestCase(TestCase):
    def addNewImageBasicPlan(self):
        Image.objects.create(image="C:\Users\Kursat Aslan\OneDrive\Resimler\Ekran Görüntüleri\2022-05-13.png"
        , owner=1)
    def addGifNotImage(TestCase):
        Image.objects.create(image="C:\Users\Kursat Aslan\OneDrive\Resimler\Ekran Görüntüleri\gif_image.gif"
        , owner=1)
    def addNewImagePremiumPlan(self):
        Image.objects.create(image="C:\Users\Kursat Aslan\OneDrive\Resimler\Ekran Görüntüleri\2022-05-13.png"
        , owner=2)
    def addNewImageEntrPlan(self):
        Image.objects.create(image="C:\Users\Kursat Aslan\OneDrive\Resimler\Ekran Görüntüleri\2022-05-13.png"
        , owner=3)
    # it try to add new image but expiretime is not in validate range
    def addNewNotExpireImageEntrPlan(self):
        Image.objects.create(image="C:\Users\Kursat Aslan\OneDrive\Resimler\Ekran Görüntüleri\2022-05-13.png"
        , owner=3,expireTime=144)
       
    # it try to add new image expiretime is in validate range
    def addNewExpireImageEntrPlan(self):
        Image.objects.create(image="C:\Users\Kursat Aslan\OneDrive\Resimler\Ekran Görüntüleri\2022-05-13.png"
        , owner=3,expireTime=144)