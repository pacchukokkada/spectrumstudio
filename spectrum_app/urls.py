"""new_spectrum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('films/',views.films,name="films"),
    path('map/',views.map,name="map"),
    path('gallery/',views.gallery,name="gallery"),
    # path('photos/<str:name>/',views.showcasephoto,name="photos"),
    path('gallery/photo_show/<str:name>/',views.PhotoShow,name="photo_show"),
    path('photo_show/<str:name>/',views.PhotoShow,name="photo_show2"),
    path('book/',views.Booking,name="book"),
    path('phototypes/<str:type>/',views.Show_by_type,name="photo_types"),
    path('about/photographer/<str:name>/',views.photographer,name="photographer"),
]
