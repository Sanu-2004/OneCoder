from django.shortcuts import render, HttpResponse, redirect
from user.models import Contact, Blog
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os



# Create your views here.
def base(request):
    return render(request, "base.html")

def index(request):
    page=request.GET.get('page')
    blogs=Blog.objects.all().order_by('date').reverse()
    p = Paginator(blogs, 4, orphans=1)
    try:
        page_obj = p.get_page(page)  
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return render(request, "index.html",{'blog':page_obj})

def about(request):
    return render(request, "about.html")

def popular(request):
    blog=Blog.objects.all().order_by('views').reverse()[:4]
    return render(request, "trending.html",{'blog':blog})

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('number')
        msg= request.POST.get('message')
        date=datetime.today()
        form = Contact(name=name,email=email,phone=phone,msg=msg,date=date)
        form.save()
        messages.success(request, "Your massage has been successfully sent")
    return render(request, "contact.html")


    

def loginuser(request):
    try:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/post")
            else:
                messages.error(request, "Wrong Username of Password")
                return redirect("/")
    except ValueError:
        return redirect("/")

def logoutuser(request):
    logout(request)
    return redirect('/')

def contactform(request):
    form=Contact.objects.all()
    param={
        'form' : form,
    }
    return render(request, 'contactform.html',param)

def deletecontact(request, id):
        delcontact= Contact.objects.filter(id=id)
        delcontact.delete()
        return redirect('/contactform')
    
def contactdetails(request, id):
    form=Contact.objects.get(id=id)
    param={
        'form':form
    }
    return render(request, 'contactdetails.html',param)

def post(request):
    blog=Blog.objects.all().order_by('id').reverse()
    return render(request,'post.html',{'blog':blog})

def addpost(request):
    if request.method=="POST":
        title=request.POST.get('title')
        subtitle=request.POST.get('subtitle')
        slug=request.POST.get('slug')
        image=request.FILES.get('image')
        content=request.POST.get('content')
        date=datetime.today()
        post= Blog(title=title, Subtitle=subtitle,slug=slug,img=image,content=content,date=date)
        post.save()
        return redirect('/post')
    return render(request, 'addpost.html')

def readblog(request, slug):
    blogs=Blog.objects.all().order_by('id').reverse()[:3]
    blog=Blog.objects.get(slug=slug)
    blog.views+=1
    blog.save()
    param={
        'blog':blog,
        'blogs':blogs
    }
    return render(request,'readblog.html',param)

def editblog(request):
    slug=request.GET.get('slug')
    blog=Blog.objects.get(slug=slug)
    return render(request,'editblog.html',{'blog':blog})

def updateblog(request):
    if request.method=="POST":
        id=request.POST.get('id')
        blog=Blog.objects.get(id=id)
        blog.title=request.POST.get('title')
        blog.Subtitle=request.POST.get('subtitle')
        blog.slug=request.POST.get('slug')
        image=request.FILES.get('image')
        blog.content=request.POST.get('content')
        print(image)
        if image:
            os.remove(blog.img.path)
            blog.img=image
        blog.save()
        return redirect('/post')
    
def deletepost(request):
    id=request.GET.get('id')
    blog=Blog.objects.get(id=id)
    print(blog.img)
    os.remove(blog.img.path)
    blog.delete()
    return redirect('/post')

def searchpage(request):
    blogs=[]
    key=request.GET.get('key')
    page=request.GET.get('page')
    result=Blog.objects.filter(title__icontains=key)
    blogs+=result
    result=Blog.objects.filter(Subtitle__icontains=key)
    blogs+=result
    result=Blog.objects.filter(content__icontains=key)
    blogs+=result
    # result=Blog.objects.all()
    
    blogs=set(blogs)
    p=Paginator(list(blogs),4,orphans=1)
    total=len(blogs)
    try:
        blog=p.get_page(page)
    except PageNotAnInteger:
        blog=p.page(1)
    except EmptyPage:
        blog = p.page(p.num_pages)
    
    param={
        'blog':blog,
        'total':total,
        'key':key
    }
    return render(request,'search.html',param)