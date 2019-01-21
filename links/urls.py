from django.urls import path
from . import views


urlpatterns = [
    path('userpage/link_list/', views.link_list, name='link_list'),
    path('userpage/', views.userpage, name='userpage'),
    path('', views.index, name='index'),
    path('userpage/add/', views.add, name='add'),

]