from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='home'),
    path('request',views.request,name ='request'),
    path('dashboard',views.dashboard,name ='dashboard'),
    path('add',views.add,name ='add'),
    path('check',views.check,name ='check'),
    path('logi',views.logi,name ='logi'),
    path('process',views.process,name ='process'),
    path('goback',views.goback,name ='goback'),
    path('auth',views.auth,name ='auth'),
    path('forward',views.forward,name='forward'),
    path('decline',views.decline,name='decline'),
    path('user_logout',views.user_logout,name ='user_logout'),
    ]