from django.shortcuts import render,HttpResponseRedirect
from blogs.forms import signup_form,login_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blogs.models import Post,Contact
from django.contrib.auth.models import Group


# Create your views here.

# Home page view
def home(request):
    stored_posts = Post.objects.all()
    return render(request,'blogs/index.html',{'posts':stored_posts})

# About page view
def about(request):
    return render(request,'blogs/about.html')

# Contact page view
def contact(request):
    if request.method == 'POST':
        fetched_name = request.POST['name']
        fetched_phone_no = request.POST['phone_no']
        fetched_feedback = request.POST['feedback']

        register = Contact(name=fetched_name,phone_no=fetched_phone_no,feedback=fetched_feedback)
        register.save()

        messages.success(request,'Feedback Submitted !! Thank You for your response.')
    return render(request,'blogs/contact.html')

# Signup page view
def user_signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Viewers')
            user.groups.add(group)

            messages.success(request,'You Signed up sucessfully!')
    else:
        form = signup_form()
    return render(request,'blogs/signup.html',{'form':form})
    
# Login page view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = login_form(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = login_form()
        return render(request,'blogs/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

# Dashbaord page view
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
    return render(request,'blogs/dashboard.html',{'blogs':posts,'admin_name':request.user})

# Add blog page view
def add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            gained_title = request.POST['title']
            gained_content = request.POST['desc']
            
            register_blog = Post(title=gained_title,desc=gained_content)
            register_blog.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request,'blogs/addblog.html')
    else:
        return HttpResponseRedirect('/login/')

# Edit blog page view
def edit_blog(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog = Post.objects.get(pk=id)
            edited_title = request.POST['title']
            edited_desc = request.POST['desc']
            blog.title = edited_title
            blog.desc = edited_desc
            blog.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            blog = Post.objects.get(pk=id)       
        return render(request,'blogs/editblog.html',{'blog':blog})
    else:
        return HttpResponseRedirect('/home/')

# Delete blog page view
def delete_blog(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog = Post.objects.get(pk=id)
            blog.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# Logout page view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/signup/')