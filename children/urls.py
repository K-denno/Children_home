from django.urls import path
from . import views


urlpatterns = {
    path('', views.Index, name='index_view'),
    path('authenticate/login/', views.login, name='login_view'),
    path('authenticate/register/', views.register, name='signout_view'),
}