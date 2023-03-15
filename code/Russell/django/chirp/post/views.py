from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Profile
from django.contrib import messages
from .forms import PostForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, ("You Successfully Squeaked a Squawk!"))
                return redirect('index')

        posts = Post.objects.all().order_by("-created_date")
        return render(request, 'index.html', {'posts': posts, 'form':form})
    else:
        posts = Post.objects.all().order_by("-created_date")
        return render(request, 'index.html', {'posts': posts})

def all_profiles(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'all_profiles.html', {"profiles":profiles})
    
    else:
        messages.success(request, ("Please Log In To View This Content"))
        return redirect('/')
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        posts = Post.objects.filter(author=pk).order_by("-created_date")
        
        if request.method == "POST":

            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide follow/unfollow
            if action == 'unfollow':
                current_user_profile.following.remove(profile)
            elif action == 'follow':
                current_user_profile.following.add(profile)
            # Save profile
            current_user_profile.save()



        return render(request, 'profile.html', {'profile':profile, "posts":posts})
    
    else:
        messages.success(request, ("Please Log In To View This Content"))
        return redirect('index')
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Successfully Logged In"))
            return redirect('index')
        else:
            messages.success(request, ("Please Try Again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out, Come Back Soon"))
    return redirect('index')

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Welcome, New Squawker!"))
            return redirect('index')
    
    return render(request, 'register.html', {'form':form})