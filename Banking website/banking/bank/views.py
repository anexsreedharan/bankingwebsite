from django.shortcuts import render
from . models import bank
# Create your views here.
def Home(request):
    return render(request,'index.html')
def login_page(request):
    return render(request,'login_page.html')
def Register_page(request):
    bank_items=bank.objects.all()
    return render(request,'register.html',{'bank_details':bank_items})
def form_page(request):
    return render(request,'form_page.html')
def final_page(request):
    return render(request,'final_page.html')
def Register2(request):
    return render(request,'register2.html')