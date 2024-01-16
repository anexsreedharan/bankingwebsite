from django.urls import path
from . import views
app_name='bank'
urlpatterns = [

    path('',views.Home,name='home'),
    path('login/',views.login_page,name='login_page'),
    path('register/',views.Register_page,name='register'),
    path('form/',views.form_page,name='forms'),
    path('final/',views.final_page,name='final'),
    path('register2/',views.Register2,name='register2')
]
