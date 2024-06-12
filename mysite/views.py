from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request=request,template_name='index.html')

def about_view(request):
    return render(request=request,template_name='about.html')

def contact_view(request):
    return render(request=request,template_name='contact.html')

def shop_view(request):
    return render(request=request,template_name='shop.html') 

def skating_view(request):
    return render(request=request,template_name='skating.html')