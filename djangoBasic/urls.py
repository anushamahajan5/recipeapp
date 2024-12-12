"""
URL configuration for djangoBasic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from DjangoApp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from DjangoApp import views

urlpatterns = [
    path('', index, name="home"),
    path('recipes/', recipes, name="recipes"),

    path('delete-recipe/<int:id>/',views.delete_recipe, name="delete_recipes"),
    path('update-recipe/<int:id>/',views.update_recipe, name="update_recipe"),
    path('contact/', contact, name="about"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('about/', about, name="about"),
    path('logout/', logout_page, name="logout_page"),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    
urlpatterns+=staticfiles_urlpatterns()