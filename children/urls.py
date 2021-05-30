from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index_view'),
<<<<<<< HEAD
]
=======
    path('guardians/', views.guardians, name='guardians_view'),
    path('guardian/<int:pk>/', views.one_guardian, name='guardian_view'),
    path('children/', views.children, name='children_view'),
    path('child/<int:pk>/', views.one_guardian, name='child_view'),
    path('authenticate/login/', views.login, name='login_view'),
    path('authenticate/register/', views.register, name='signout_view'),
]
>>>>>>> a559888 (completed backend)
