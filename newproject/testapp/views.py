from django.shortcuts import render,redirect
from testapp.models import Login
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def login(request):
    if(request.method=="POST"):
        user=request.POST.get('user')
        passw=request.POST.get('passw')
        print(user)
        print(passw)
        user=authenticate(request,username=user,password=passw)
        print(user)
        if user is not None:
            print('popppp')
            login(request,user)
            return redirect('/ibm/')
        else:
            return HttpResponse('Sorry Bad One')

    return render(request,'testapp/login.html')

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        uname=request.POST.get('user_name')
        em=request.POST.get('email') 
        passw=request.POST.get('passw') 
        repassw=request.POST.get('repassw')
        Login.objects.get_or_create(fname=fname,lname=lname,uname=uname,em=em,passw=passw,repassw=repassw)

        return redirect ('/login/')
        
        


    return render(request,'testapp/signup.html')


def ibm(request):
    return render(request,'testapp/ibm.html')