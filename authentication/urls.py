from django.contrib import admin
from django.urls import path
from authentication import urls
from django.conf.urls import include, url
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/' , views.RegisterApi.as_view(), name = 'create-user'),
    url(r'^login/', views.Login.as_view(), name='login'),
    path('updatePic/<int:pk>/', views.Update_profile.as_view(), name='all-profiles'),
    path('getPic/<int:pk>/', views.Individual_profile.as_view(), name='all-profiles'),
    path('getAllPics/', views.Profile_pictures.as_view(), name='all-profiles'),
    path('getMyPic/', views.My_profile.as_view(), name='all-profiles'),



]
