"""
URL configuration for escuela_Edutec project.

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
from django.urls import path, include
from dark_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('edu_app.urls')),
    path('cursos/', include('cursos.urls')),
    path('estudiantes/', include('estudiantes.urls')),
    path('reportes/', include('reportes.urls')),
    path('toggle_theme/', views.toggle_theme, name='toggle_theme'),
   ]
