from django.db import models


# Create the database table 
class Post(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=160)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title