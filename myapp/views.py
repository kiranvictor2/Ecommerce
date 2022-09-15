
from ast import Return
from email.policy import default
from posixpath import split
from urllib import request, response
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import datarow, datas,Userper, person
from .forms import cartt, helpp, login,replay,newuser,relay
from django.shortcuts import render  

#-----------------------------------------------------------ADMIN CONTENTS----------------------------------------------------------
# Create your views here.


def workbase(request):
    v=replay()
    if(request.method=="POST"):
        v=replay(request.POST,request.FILES)
        if(v.is_valid()):
            v.save()
            return redirect(shows)
    return render(request,"workbase.html",{"ror":v})


def shows(request):
    haa=datas.objects.all()
    return render(request,"verification.html",{"jek":haa})

def emai(request):
    receive='kiranvictor2@gmail.com'
    sub="datacorriders"
    msg='harry is the secular person'
    send_mail(sub,msg,settings.EMAIL_HOST_USER,[receive])
    HttpResponse

def support(request):
    v= helpp()
    if(request.method=="POST"):
            v=helpp(request.POST)
            if(v.is_valid()):
                Email=v.cleaned_data.get('email')
                sub=v.cleaned_data.get('subject')
                msg=v.cleaned_data.get('msg')
                send_mail(sub,msg,settings.EMAIL_HOST_USER,[Email])
    return render(request,"pass.html",{"ror":v})

    
def emai(request):
    receive='kiranvictor2@gmail.com'
    sub="datacorriders"
    msg='harry is the secular person'
    send_mail(sub,msg,settings.EMAIL_HOST_USER,[receive])

def dell(request,pk):
    gg=datarow.objects.get(pk=pk)
    gg.delete()
    return redirect(shows)


def update(request,pk):
    dele=datas.objects.get(pk=pk)
    form=replay(instance=dele)
    if(request.method=="POST"):
        form=replay(request.POST,request.FILES,instance=dele)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect(shows)
    return render(request,"workbase.html",{"ror":form})

def showme(request,pk):
    dele=datarow.objects.get(pk=pk)
    form=replay(instance=dele)
    if(request.method=="POST"):
        form=replay(request.POST,request.FILES,instance=dele)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect(shows)
    return render(request,"show.html",{"ror":dele})


#-----------------------------------------------------------USER CONTENTS----------------------------------------------------
#--------------------------------------------------------------Registration---------------------------------------------------------

def register(request):
    v=newuser()
    if(request.method=="POST"):
        v=newuser(request.POST,request.FILES)
        if(v.is_valid()):
            v.save()
            return redirect(mainsite)
    return render(request,"register.html",{"ror":v})


#--------------------------------------------------------------Login---------------------------------------------------------

def log(request):
    v= login()
    haa=datas.objects.all()
    if('username' in request.session):
        return redirect(mainsite)
    if(request.method=="POST"):
            v=login(request.POST)
            if(v.is_valid()):
                user=v.cleaned_data.get('username')
                pwd=v.cleaned_data.get('password')
                if(Userper.objects.filter(username=user) and Userper.objects.filter(password1=pwd)):
                    cust=Userper.objects.get(username=user)
                    ver=cust.username
                    request.session['username']=ver
                    return redirect(mainsite)
                else:
                    return HttpResponse("error") 
    return render(request,"login.html",{"ror":v})


def logout(request):
    if('username' in request.session):
        request.session.flush()
    return redirect(mainsite)

#--------------------------------------------------------------Home route---------------------------------------------------------

def mainsite(request):
    haa=datas.objects.all()
    if 'username' in request.session:
        ca=request.session['username']
        user=Userper.objects.get(username=ca)
        return render(request,"index.html",{"jek":haa,"user":user})
    else:
        return redirect(log)


def data(request):
    v=relay()
    if 'username' in request.session:
        ca=request.session['username']
        user=Userper.objects.get(username=ca)
        if(request.method=="POST"):
            v=relay(request.POST,request.FILES)
            if(v.is_valid()):
                v.save()
                return redirect(shows)
    return render(request,"adddata.html",{"ror":v,"user":user})

    
def sentdata(request,pk):
    if 'username' in request.session:
        ca=request.session['username']
        user=Userper.objects.get(username=ca)
        cat=datas.objects.get(id=pk)
        categor=cat.category.lower()
        dat=datarow.objects.filter(category=categor)
    return render(request,"list.html",{"alldata":dat,"user":user})

def sentcar(request):
    v=cartt()
    if cartt(request.method=="POST"):
        v=cartt(request.POST)
        if(v.is_valid()):
            v.save()
    return render(request,"listcart.html",{"ror":v})


def showcart(request):
    if 'username' in request.session:
        ca=request.session['username']
        ga=person.objects.filter(firstname=ca)
        for i in ga:
            k=i.lastname
            pa=datarow.objects.filter(id=k)
            context={'ror':pa}
        print(context)
    return render(request,"cart.html",{"ror":ga})
            