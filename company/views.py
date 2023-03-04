from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, ProductDemo
from .forms import ContactForm
from django.db.models import Q 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def Homepage(request):

    # Query all posts
    all_posts = Post.objects.all()

    return render(request, 'company/home.html', {'all_posts': all_posts})


def post_detail(request, id):
    # Query 1 post
    single_post = Post.objects.get(id=id)
    return render(request, 'company/post-detail.html', {'single_post': single_post})


def about(request):
    data = ProductDemo.objects.all() # --> SELECT * from company_productdemo
    context = {'data':data} # attachment
    return render(request, 'company/about.html',context)


def product(request):
    data = ProductDemo.objects.all() 
    context = {'data':data} 
    return render(request, 'company/product.html',context)


def contact(request):
    # Check the incoming request
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB
            form.save()
            return redirect("/")
    else:
        form = ContactForm()

    return render(request, 'company/contact.html', {'form': form})


def search(request):
    # Get the incoming query params
    search_post = request.GET.get('q')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post))
    else:
        pass
    return render(request, 'company/search.html', {'posts': posts})


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request, 
            username=username,
            password=password
        )

        if user is not None:
            # Log user in
            login(request, user)
            return redirect('/')
        messages.error(request, 'Invalid Login')

    return render(request, 'company/sign-in.html')


def sign_out(request):
    # Sign user out
    logout(request)
    return redirect('/sign-in')










