from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, ProductDemo

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
    data = ProductDemo.objects.all() # --> SELECT * from company_productdemo
    context = {'data':data} # attachment
    return render(request, 'company/product.html',context)