from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('contact/', views.contact_us, name="contact"),
    path('about/', views.about,name="about"),
       path('', include('myapp.urls')), 
        path('register/', views.register, name='register'),
]