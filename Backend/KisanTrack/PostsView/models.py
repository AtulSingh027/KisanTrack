from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    Description = models.TextField()
    image = models.ImageField(upload_to='images/PostImages/',null=True, blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category} - {self.price} - {self.created_at}"
