from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # New
from django.conf.urls.static import static  # New




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),  # Our app
    path('summernote/', include('django_summernote.urls'))  # Summernote
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
