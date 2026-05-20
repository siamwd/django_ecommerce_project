from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    class Meta: 
        verbose_name_plural = "categories"
# Create your models here.
    def __str__(self):
        return self.name
class Product(models.Model):
    
    category = models.ForeignKey(Category , related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', blank=True)
    
    def __str__(self):
        return self.name