from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('order/', views.index, name = 'order'),
    path('addtoshopcart/', views.addtoshopcart, name = 'addtoshopcart'),
    path('shopcart/', views.shopcart, name = 'shopcart'),
    path('deletefromcart/<str:id>', views.deletefromcart, name = 'deletefromcart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('ordercompleted/', views.ordercompleted, name = 'ordercompleted'),
    path('placeorder/', views.placeorder, name = 'placeorder'),
]