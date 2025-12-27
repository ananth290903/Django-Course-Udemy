from django.db import models

class Review(models.Model):
    user_name=models.CharField(max_length=100)
    review_text=models.TextField()
    rating=models.IntegerField()

    def __str__(self):
        return f"{self.user_name} posted a review  of {self.rating}"
