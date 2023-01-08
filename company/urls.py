from django.urls import path
from .views import Homepage, about  # Import the functions from views.py


urlpatterns = [
    # path('URL Name', Function)
    path('', Homepage),
    path('about', about)
]