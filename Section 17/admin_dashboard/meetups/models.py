from django.db import models

class Meetup(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return f"{self.title}:({self.slug})"
    

