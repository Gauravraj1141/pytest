from django.shortcuts import render, redirect
from .forms import User_register_form, User_login_form, User_blog_form
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import User_Blog


# homepage

def homepage(request):
    blogdata = User_Blog.objects.all()
    if request.user.is_authenticated:
        login = True
        return render(request, "blogapp/home.html", {"login": login, 'blog': blogdata})
    else:
        login = False
        return render(request, "blogapp/home.html", {"login": login, 'blog': blogdata})


# user register

def User_register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fmdata = User_register_form(request.POST)
            if fmdata.is_valid():
                fmdata.save()
                messages.success(request, 'User have been registered')
                return redirect("login")
        else:
            fmdata = User_register_form()
        return render(request, "blogapp/signup.html", {"form": fmdata})
    else:
        return redirect("/profile/")


# user login

def User_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fmdata = User_login_form(request=request, data=request.POST)
            if fmdata.is_valid():
                uname = fmdata.cleaned_data["username"]
                psw = fmdata.cleaned_data["password"]
                realuser = authenticate(username=uname, password=psw)
                if realuser is not None:
                    login(request, realuser)
                    messages.success(request, "login successfully")
                    return redirect("/profile/")
        else:
            fmdata = User_login_form(request=request)

        return render(request, "blogapp/login.html", {"form": fmdata})
    else:
        return redirect("/profile/")


# user logout


def User_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    else:
        return redirect("register")


# User Profile

def User_profile(request):
    if request.user.is_authenticated:
        firstname = request.user.first_name
        username = request.user.username
        lastname = request.user.last_name
        if len(firstname) > 3 and len(lastname) > 2:
            author = f"{firstname} {lastname}"
        else:
            author = username
        blogdata = User_Blog.objects.filter(Author=author)
        context = {"blogs": blogdata, "name": author}
        return render(request, "blogapp/profile.html", context)

    else:
        return redirect("/")


# for show edit and add blog by authenticated user

def User_Add_blog(request):
    if request.user.is_authenticated:
        firstname = request.user.first_name
        username = request.user.username
        lastname = request.user.last_name
        if request.method == "POST":
            blog_form = User_blog_form(request.POST)
            if blog_form.is_valid():
                title = blog_form.cleaned_data["Title"]
                desc = blog_form.cleaned_data["Desc"]
                if len(firstname) > 3 and len(lastname) > 2:
                    author = f"{firstname} {lastname}"
                else:
                    author = username
                blogdata = User_Blog(Title=title, Desc=desc, Author=author)
                blogdata.save()
                messages.success(request, "Your blog added successfully")
                return redirect("/profile/")
        else:
            blog_form = User_blog_form()

        return render(request, "blogapp/Addblog.html", {"form": blog_form, "name": request.user})
    else:
        return redirect("login")


# read blog by authenticated user

def User_read_blog(request, id):

    if request.user.is_authenticated:
        getblog = User_Blog.objects.get(U_id=id)
        return render(request, "blogapp/read_blog.html", {"blog": getblog})
    else:
        return redirect("login")


# update blog


def User_Update_blog(request, id):

    if request.user.is_authenticated:
        if request.method == "POST":
            blogdata = User_Blog.objects.get(U_id=id)
            updateform = User_blog_form(request.POST, instance=blogdata)
            if updateform.is_valid():
                updateform.save()
                messages.success(request, "Your Blog Updated Successfully !")
                return redirect("/profile/")
        else:
            blogdata = User_Blog.objects.get(U_id=id)
            updateform = User_blog_form(instance=blogdata)
        return render(request, "blogapp/update.html", {"form": updateform})


# delete blog

def User_Delete_blog(request, id):

    if request.user.is_authenticated:
        blogupdatedata = User_Blog.objects.get(U_id=id)
        blogupdatedata.delete()
        messages.success(request, "This blog has been deleted!")
        return redirect("/profile/")


# about page

def about_blog(request):
    if request.user.is_authenticated:
        login = True
        return render(request, "blogapp/about.html", {"login": login})
    else:
        login = False
        return render(request, "blogapp/about.html", {"login": login})
