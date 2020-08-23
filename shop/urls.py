from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='Login'),
    path('home', views.home,name='Home'),
    path('profile',views.profile,name='Profile'),
    path('update_profile',views.update_profile,name='Update Profile'),
    path('register',views.register,name='Register'),
    path('validate',views.validate,name='Validate'),
    path('other',views.other,name='Other'),
    path('add_to_kart',views.add_to_kart,name='Add to Kart'),
    path('home1',views.home1,name='Home'),
    path('mykart',views.mykart,name="Mykart"),
    path('logout',views.logout,name='Logout'),
    path('admin',views.admin,name='Admin'),
    path('checkout',views.checkout,name='Checkout'),
    path('complete_order',views.complete_order,name='Complete Order')
]