from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='post_images/%Y/%m/%d', null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.rate}'