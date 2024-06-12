from django.urls import path
from  .views import home_view,about_view,contact_view,shop_view,skating_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('contact/',contact_view,name='contact-page'),
    path('shop/',shop_view,name='shop-page'),
    path('skating/',skating_view,name='skating-page'),
]