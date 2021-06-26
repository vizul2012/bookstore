from django.shortcuts import render,redirect
from.models import *
# Create your views here.
def Registerpage(request):
    return render(request, "app/regration.html")

def Loginpage(request):
    return render(request,"app/login.html")

def Registeruser(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        pwd = request.POST['passwd']

        slr = seller.objects.create(fname=fn,lname=ln,email=em,passwd=pwd)

        return redirect("Loginpage")
    else:
        msg = "method changes"
        return render(request,"app/regration.html",{'err':msg})


def Loginuser(request):
    em = request.POST['email']
    pwd = request.POST['passwd']

    user = seller.objects.filter(email=em)

    if len(user) > 0:
        if user[0].passwd == pwd:
            return redirect("indexpage")
        else:
            msg = "Password is Incorrect..!"
            return render(request, "app/login.html",{'err':msg})
    else:
        msg = "Seller Doesn't Found"
        return render(request, "app/login.html",{'err':msg})


	
	
	

 
 
