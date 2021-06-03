from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index_view'),
    path('guardians/', views.guardians, name='guardians_view'),
    path('guardian/<int:pk>/', views.one_guardian, name='guardian_view'),
    path('children/', views.children, name='children_view'),
    path('child/<int:pk>/', views.one_guardian, name='child_view')
]
