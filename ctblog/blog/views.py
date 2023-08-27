from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Blog,Contacts
# Create your views here.
@login_required(login_url='login')
def home_page(request):
    context ={}
    blogs =Blog.objects.all()
    context["blogs"] = blogs  
    return render(request,"home.html",context)

def cntact_us(request):
    context = {}
    if request.POST:
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            my_form.save()
        else:
            context["errors"] = my_form.errors


    return render(request,"contact-us.html",context)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2 :
            return HttpResponse("Your password and confrom password are not Same!!")
        
            

            
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('blog:login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("blog:home")
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('blog:login')

