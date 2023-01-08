from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def Homepage(request):
    # Query all posts
    all_posts = Post.objects.all()

    return render(request, 'company/home.html', {'all_posts': all_posts})


def about(request):
    return render(request, 'company/about.html')



