from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        gender_type=request.POST.get("gender_type")
        Profile_Pic=request.FILES.get("Profile_Pic")
        contact_no=request.POST.get("contact_no")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                gender_type=gender_type,
                Profile_Pic=Profile_Pic,
                contact_no=contact_no,
            )
           
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")

def addperson(request):


  
    if request.method=='POST':
            jobs=PERSONMODEL()
            jobs.name=request.POST.get("name")
            jobs.profession=request.POST.get("profession")
            jobs.image=request.FILES.get("image")
            jobs.contact_no=request.POST.get("contact_no")
            jobs.email=request.POST.get("email")
            jobs.gender_type=request.POST.get("gender_type")
            jobs.address=request.POST.get("address")
            jobs.country=request.POST.get("country")
            jobs.bio=request.POST.get("bio")
            jobs.occupation=request.POST.get("occupation")

           
            jobs.save()
       
    
    return render(request,"addperson.html")

def showperson(request):

    jobs=PERSONMODEL.objects.filter()

    context= {
        'jobs': jobs
    }
    
    return render(request,"showperson.html",context)

def personfeed(request):

   
    jobs=PERSONMODEL.objects.all()

    context= {
        'jobs': jobs
    }
    
    return render(request,"personfeed.html",context)

def deletejob(request,job_id):

    jobs=PERSONMODEL.objects.filter(id=job_id)
    jobs.delete()

    
    return redirect("createjob")


def viewjob(request,job_id):

    jobs=PERSONMODEL.objects.filter(id=job_id)

    context= {
        'jobs': jobs
    }
    
    
    return render(request,"viewjob.html",context)

def editjob(request,job_id):

    jobs=PERSONMODEL.objects.get(id=job_id)

    context= {
        'jobs': jobs
    }

    current_user=request.user
    if current_user.user_type == "recruiter":
        if request.method=="POST":
            jobs=PERSONMODEL()
            jobs.id=request.POST.get("job_id")
            jobs.name=request.POST.get("name")
            jobs.profession=request.POST.get("profession")
            jobs.image=request.FILES.get("image")
         
            
            jobs.save()
           
            return redirect("createjob")
    
    return render(request,"editjob.html",context)


def apply_now(request,id):
    curernt_user=request.user
    if curernt_user.user_type == 'seeker':


        jobs=JobModel.objects.get(id=id)

        context= {

            'jobs': jobs
        }

        
      
        if request.method == 'POST':
            job_title=request.POST.get('job_title')
            Resume=request.FILES.get('Resume')
            Cover=request.POST.get('Cover')
            skills=request.POST.get('skills')
            job_Pic=request.FILES.get('job_Pic')

            apply=jobApplyModel(
                user=curernt_user,
                job_title=jobs,
                skills=skills,
                Resume=Resume,
                Cover=Cover,
                job_Pic=job_Pic,

               
            )
            apply.save()

            
            return redirect('jobfeed')

          


        return render(request,'apply_now.html',context)
    

def searchJob(request):
    
    query = request.GET.get('query')
    
    if query:
        
        jobs=JobModel.objects.filter(Q(job_title=query) 
                                       |Q(category=query)
                                       |Q(skills=query)) 
                                       
    
    else:
        jobs = JobModel.objects.none()
        
    context={
        'jobs':jobs,
        'query':query
    }
    
    return render(request,"searchJob.html",context)
