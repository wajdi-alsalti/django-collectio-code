from django.shortcuts import redirect, render
from .models import Profile
from .forms import UserForm,ProfileForm,SignUpForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def profileUser(request):
    # user is the fields in Profile models
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

# this function let us edit the user information receive the data from User class
# and from Profile class we created 
def profileEdit(request):
    # user is the fields in Profile models
    profile = Profile.objects.get(user= request.user)
    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = ProfileForm(request.POST, request.FILES,instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myProfile = profileForm.save(commit=False)
            myProfile.user = request.user
            myProfile.save()
            return redirect(reverse('account:profile'))
    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userForm,'profileForm':profileForm})


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() :
            form.save()
            
#after save update section to login and take username and pass to login
# form.cleaned_data it is allow to fetch data from the form we use it like dict 
# print form.cleaned_data to show the fields u want
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user1 = authenticate(username=username,password=password)
#after update and authenticate make login function in django
            login(request,user1)
            return redirect('account:profile')

    else:
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})
