from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Product(models.Model):
    image = models.ImageField(upload_to='post_images', null=True,blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(
        Category,
        related_name='products'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner',
        null=True
    )

    def __str__(self):
        return f'{self.title} - {self.rate}'

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sender',
        null=True
    )



    def __str__(self):
        return f'Comment for {self.product.title}'