from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView

handler404 = 'links.views.error404'

urlpatterns = [
    path('userpage/list/', views.list, name='list'),
    path('userpage/', views.userpage, name='userpage'),
    path('userpage/list/<tag>/', views.tagview, name='tagview'),
    path('userpage/search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('userpage/add/', views.add, name='add'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'login/$', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('userpage/remove/<pk>/', views.remove, name='remove'),
    path('userpage/edit/<pk>/', views.edit, name='edit'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^about/$', views.about, name='about'),

]