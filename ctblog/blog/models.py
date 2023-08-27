from django.db import models

# Create your models here.

class Blog(models.Model):
     title = models.CharField(max_length=255)
     description = models.TextField()
     image = models.ImageField(upload_to="blog_posts/", default=None, null=True, blank=True)

     def __str__(self):
        return self.title


class Contacts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
   

    def __str__(self):
        return self.first_name + " - "+  self.email + "-" + self.message