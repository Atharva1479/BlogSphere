from django.shortcuts import render
from .models import Post
from django.http import request
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import PostForm 
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts' : posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post' : post})

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User created successfully')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')  
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')  
 

@login_required
def user_dashboard(request):
    # Fetch posts created by the logged-in user
    posts = Post.objects.filter(author=request.user)  

    return render(request, 'dashboard.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('dashboard')  
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
