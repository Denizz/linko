from django.urls import path
from . import views


urlpatterns = [
    path('link_list/', views.link_list, name='link_list'),
    path('', views.index, name='index'),

]