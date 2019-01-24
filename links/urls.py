from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('userpage/link_list/', views.link_list, name='link_list'),
    path('userpage/', views.userpage, name='userpage'),
    path('', views.index, name='index'),
    path('userpage/add/', views.add, name='add'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^login/$', LoginView.as_view(), {'next_page': settings.LOGIN_REDIRECT_URL}, name='login'),
    path('userpage/remove/', views.remove, name='remove'),
    path('newuser/', views.newuser, name='newuser'),

]