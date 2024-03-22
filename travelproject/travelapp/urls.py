from . import views
from django.urls import path

urlpatterns = [
    # path('',views.home,name='home'),
    # path('thanks', views.thanks, name='thanks'),



    path('', views.detail, name='detail'),
    path('registration/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # path('about/', views.about, name='about'),
    # path('add/', views.addition, name='add')

]
