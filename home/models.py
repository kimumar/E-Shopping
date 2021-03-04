from django.db import models

from django.forms import Textarea, TextInput
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Setting(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=50, null=True)
    address = models.CharField( max_length=100)
    phone = models.CharField( null=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(blank=True,null=True,  upload_to='images/')
    logo = models.ImageField(blank=True,null=True, upload_to='images/')
    banner = models.ImageField(blank=True,null=True, upload_to='images/')
    spinner =  models.ImageField(blank=True,null=True, upload_to='images/')
    spinner2 =  models.ImageField(blank=True,null=True, upload_to='images/')
    spinner3 =  models.ImageField(blank=True,null=True, upload_to='images/')
    gotop =  models.ImageField(blank=True,null=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    about =RichTextUploadingField(blank=True)
    contact =RichTextUploadingField(blank=True)
    refrences =RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    
    def __str__(self):
        return self.title


class Client(models.Model):
    title = models.CharField(max_length=10,blank=True,null=True)
    clients = models.ImageField(blank=True,null=True, upload_to='images/')    

    def __str__(self):
        return self.title

    
class Slider(models.Model):
    title = models.CharField(max_length=50)
    slide =  models.ImageField(null=True, blank=True, upload_to='images/')  
    slides =  models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets= {
            'name' : TextInput(attrs={'class': 'input', 'placeholder': 'Name and Surname'}),
            'subject' : TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email' : TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'message' : Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
        }