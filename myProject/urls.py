from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/",signInPage, name="signInPage"),
    path("homePage/",homePage, name="homePage"),
    path("logoutPage/",logoutPage, name="logoutPage"),
    path("ProfilePage/",profilePage, name="profilePage"),
    path("addperson/",addperson, name="addperson"),
    path("showperson/",showperson, name="showperson"),
    path("personfeed/",personfeed, name="personfeed"),
    path("deletejob/<int:job_id>",deletejob, name="deletejob"),
    path("viewjob/<int:job_id>",viewjob, name="viewjob"),
    path("editjob/<int:job_id>",editjob, name="editjob"),
    path("apply_now/<int:id>", apply_now, name="apply_now"),
    path('searchJob/',searchJob, name='searchJob'),
   

   

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
