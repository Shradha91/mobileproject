from django.urls import path

from . import views

urlpatterns = [
    path('', views.mobile_list, name='index'),
    path('mobiles/<slug:slug>/', views.mobile_detail, name='mobile_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name='contact'),
]
