from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index_view'),
    path('guardians/', views.guardians, name='guardians_view'),
    path('guardian/<int:pk>/', views.one_guardian, name='guardian_view'),
    path('children/', views.children, name='children_view'),
    path('child/<int:pk>/', views.one_child, name='child_view'),
    path('searchchild/', views.search_child, name='search_child'),
    path('searchguardian/', views.search_guardian, name='search_guardian'),
    path('updateguardian/', views.update_guardian, name='update_guardian'),
    path('updatechild/', views.update_child, name='update_child'),
]

