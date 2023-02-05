from django.contrib import admin
from .models import Post, ProductDemo, Contact
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)  
    list_display = ['title', 'date_created', 'date_updated']


# admin.site.register(Model, ModelAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ProductDemo)
admin.site.register(Contact)
