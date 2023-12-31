"""teacherdirectory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from directoryapp import views as dt
# from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dt.index, name='index'),
    path('logout/', dt.logout, name='logout'),

    path('LoginCheck/', dt.LoginCheck, name='LoginCheck'),
    path('apphome/', dt.apphome, name='apphome'),
    path('importedForm/', dt.importedForm, name='importedForm'),
    path('importBulk/', dt.importBulk, name='importBulk'),
    path('DataView/', dt.DataView, name='DataView'),
    path('TeacherDirectoryForm/', dt.TeacherDirectoryForm,
         name='TeacherDirectoryForm'),
    path('FilterTeacherProfile/', dt.FilterTeacherProfile,
         name='FilterTeacherProfile'),
    path('GetProfilePage/', dt.GetProfilePage, name='GetProfilePage'),
    path('AddTeacherData/', dt.AddTeacherData, name="AddTeacherData"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
