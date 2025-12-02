from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator 
from django.urls import reverse
from django.utils.text import slugify


# class Author(models.Model):
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)


# class Book(models.Model):
#     title=models.CharField(max_length=50)
#     rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
#     author=models.ForeignKey(Author,on_delete=models.CASCADE ,null=True, related_name="books")
#     isBestSeller=models.BooleanField(default=False)
#     slug=models.SlugField(default="",null=False)

#     def get_absolute_url(self):
#         return reverse("book_in_detail",args=[self.slug])
    
#     def save(self,*args,**kwargs):
#         self.slug=slugify(self.title)
#         super().save(*args,**kwargs)        

#     def __str__(self):
#         return (f"{self.title}:({self.rating})")


class Book(models.Model):
    title=models.CharField(max_length=50,editable=True)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.CharField(null=True,max_length=100,editable=False)
    isBestSeller=models.BooleanField(default=False)
    slug=models.SlugField(default="",null=False,db_index=True,primary_key=True)

    def __str__(self):
        return (f"{self.title}:({self.rating})")
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("book_detailed",args=[self.slug])
    



