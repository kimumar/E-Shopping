from django.db import models

from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})



class Product(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )

    AVAILABLE =(
        ('In Stock', 'In Stock'),
        ('Out Of Stock', 'Out Of Stock'),
        ('ReStocked', 'ReStocked'),
    )
    
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150, blank=True)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image= models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField(null=True, blank=True)
    discount_price= models.FloatField(blank=True, null=True)
    available= models.CharField(choices=AVAILABLE, max_length=15, default='In Stock')
    brand= models.CharField( max_length=30,null=True, blank=True)
    code= models.CharField( max_length=30,null=True, blank=True)
    points= models.CharField( max_length=30,null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    quantity_instock = models.IntegerField(null=True, blank=True, default=1000)
    minquantity = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bestseller = models.BooleanField(blank=True)
    topseller = models.BooleanField(blank=True)
    trending = models.BooleanField(blank=True)
    featured = models.BooleanField(blank=True)
    new =models.BooleanField(blank=True)
    banner = models.BooleanField(blank=True)
    latest = models.BooleanField(blank=True)
    detail = RichTextUploadingField()
    
    
    def __str__(self):
        return self.title

    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})     


class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING, null=True, blank=True)
    title=models.CharField(max_length=50, blank=True)
    image= models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title 
    