from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', views.user_list, name ="users"),# list all users
    path('image/<str:pk>', views.image_list, name ="images"),# list all images user has
    path('imageupload', views.uploadImage, name = 'uploadImage'),# it for upload an image
    path('images/static/images/', views.image_url, name = 'image_url'),# it for upload an image
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)