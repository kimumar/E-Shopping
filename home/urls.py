from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('refrences/', views.refrences, name='refrences'),
    path('category/<str:id>/<slug:slug>', views.category_prod, name='category_prod'),
    path('product/<str:id>/<slug:slug>', views.prod_detail, name='prod_detail'),   
    
]