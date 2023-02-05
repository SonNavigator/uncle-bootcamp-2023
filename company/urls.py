from django.urls import path
from .views import (
    Homepage, about, product, post_detail,
    contact, search
)

urlpatterns = [
    path('', Homepage), # localhost:8000
    path('about', about),
    path('product', product),
    path('blog/<int:id>', post_detail),
    path('contact', contact),
    path('search', search)
]