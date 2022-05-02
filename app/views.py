from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from itsdangerous import serializer
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect("/home/")
    else:
        if request.method=="GET":
            form = SignupForm()
            return render(request,"app/signup.html",{'form':form})
        else:
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                usr=request.POST.get('username')
                U=User.objects.get(username=usr)
                print(U)
                print(U.id)
                print(U.username)
                P=Profile(user=U,balance=0,is_active=False)
                P.save()
                print(P)
                return redirect("/login/")
            else:
                return render(request,"app/signup.html",{"form":form})



def user_login(request):
    if request.user.is_authenticated:
        return redirect("/home/")
    else:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    
                    request.session['userId']=user.id
                    request.session['userName']=uname
                    login(request,user)

                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:	
                        return HttpResponseRedirect('/home/')
        else:			
            fm=AuthenticationForm()
        return render(request,'app/login.html',{'form':fm})



@login_required(login_url='/login/')
def home(request):
    E=Expense(user=request.user)
    P=Profile.objects.get(user=request.user)
    print(E)
    if P.is_active == True:
        if request.method=='POST' and request.POST.get('a'):
            amount=request.POST.get('amount')
            exp_type="positive"
            E.amount=float(amount)
            E.exp_type=exp_type
            E.save()
            P.balance+=float(amount)
            P.save()
            return redirect('/home/')

        elif request.method=='POST' and request.POST.get('b'):
            amount=request.POST.get('amount')
            if float(amount)>P.balance:
                messages.warning(request,"Cannot withdraw more then balance limit!")
                return redirect("/home/")
            else:
                E.amount=float(amount)
                E.exp_type="negative"
                E.save()
                P.balance-=float(amount)
                P.save()
                return redirect('/home/')

    Exp=Expense.objects.filter(user=request.user).order_by('-id')
    return render(request,'app/home.html',{"wallet_active":P.is_active,"P":P.balance,"E":Exp})


        
def user_logout(request):
    logout(request)
    return redirect('/login/')



@api_view(['GET'])
def viewBalance(request,pk): 
    try:
        user=User.objects.get(pk=pk)
        username=User.objects.get(username=user)
        print(username.id)
        print(user)
        profile = Profile.objects.get(user=user)
        print(profile)
    except Profile.DoesNotExist:
        return Response(status=404)
    if request.method=="GET":
        serializer=ProfileSerializer(profile)
        balance=(serializer.data['balance'])
        usr=(serializer.data['user'])
        user=User.objects.get(id=usr)
        username=user.username
        return Response({
            "user":usr,
            "username":username,
            "balance":balance
            })



@api_view(['POST'])
def updateBalance(request):
    if request.method=="POST":
        expense=Expense()
        profile=Profile.objects.get(user=int(request.data["user"]))
        print(profile.balance)
        user=User.objects.get(pk=(request.data["user"]))
        print(profile)
        if (request.data["expense_type"])=="income":
            expense.user=user
            expense.amount=request.data["amount"]
            expense.exp_type="positive"
            expense.save()
            exp_id=expense.id
            profile.balance += request.data["amount"]
            profile.save()
            return Response({"Msg":"Expense Created"})
        elif (request.data["expense_type"])=="expense":
            expense.user=user
            if request.data["amount"]>profile.balance:
                return Response({"Msg":"Cannot withdraw more then balance amount!"})
            expense.amount= (request.data["amount"])
            expense.exp_type="negative"
            expense.save()
            exp_id=expense.id
            profile.balance -= request.data["amount"]
            profile.save()
            return Response({"Msg":"Expense Created"})
        else:
            return Response(serializer.errors)



@api_view(["POST"])
def activateWallet(request):
    if request.method=="POST":
        us=User.objects.get(id=(request.data['id']))
        if request.data['is_active']==True:
            msg="Wallet Activated Successfully"
        else:
            msg="Wallet Deactivated Successfully"
        profile=Profile.objects.get(user=us)
        profile.is_active=request.data['is_active']
        profile.save()
        serializer=ProfileSerializer(profile)
        return Response({"msg":msg,"data":serializer.data})
