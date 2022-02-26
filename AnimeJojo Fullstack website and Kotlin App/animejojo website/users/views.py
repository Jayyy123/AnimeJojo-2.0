from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import permission_required
from .models import Profile
from .forms import ProfileForm,UserForm
from django.contrib.auth.models import User



def loginPage(request):

    if request.user.is_authenticated:
        return redirect('allanime')

    print(request.user)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"Username or Password is incorrect")
        
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('allanime')
        else:
            messages.error(request,"Username or Password is incorrect")
        
    return render(request, 'users/loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def signupPage(request):
    b = User
    a = UserForm()
    if request.method == 'POST':
        a = UserForm(request.POST)
        if a.is_valid:
            user = a.save(commit=False)
            user.save()
            login(request,user)
            return redirect('allanime')
        else:
            messages.error(request,'There was an error creating your account')

    return render(request, 'users/signupPage.html',{'a':a})

def test(request):
    return render(request, 'users/test.html')

def profile(request):
    if request.user.is_authenticated:
        username = request.user
        account = Profile.objects.get(username = username)
        
        print(account)

    return render(request, 'users/profile.html',{'a':account})
# @permission_required
def profileUpdate(request, pk):
    return render(request, 'users/profileUpdated.html')

def profileDelete(request, pk):

    return redirect('signupPage')

