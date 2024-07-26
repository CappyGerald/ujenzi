from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_view, name='project_view'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/delete/<int:pk>', views.delete_project, name='delete_project'),
    path('projects/edit/<int:pk>', views.edit_project, name='edit_project'),
    path('machinery/', views.machinery_view, name='machinery_view'),
    path('machinery/add/', views.add_machinery, name='add_machinery'),
    path('machinery/edit/<int:pk>', views.edit_machinery, name='edit_machinery'),
    path('machinery/delete/<int:pk>', views.delete_machinery, name='delete_machinery'),
    path('materials/',views.material_view, name='material_view'),
    path('materials/add/', views.add_material, name='add_material'),
    path('materials/edit/<int:pk>', views.edit_material, name='edit_material'),
    path('materials/delete/<int:pk>', views.delete_material, name='delete_material'),
    path('personel/', views.personel_view, name='personel_view'),
    path('personel/add/', views.add_personel, name='add_personel'),
    path('personel/edit/<int:pk>', views.edit_personel, name='edit_personel'),
    path('personel/delete/<int:pk>', views.delete_personel, name='delete_personel'),
    path('activity', views.activity_view, name='activity_view'),
    path('activity/add/', views.add_activity, name='add_activity'),
    path('activity/edit/<int:pk>', views.edit_activity, name='edit_activity'),
    path('activity/delete/<int:pk>', views.delete_activity, name='delete_activity'),
    path('milestone/', views.milestone_view, name='milestone_view'),
    path('milestone/add/', views.add_milestone, name='add_milestone'),
    path('milestone/edit/<int:pk>', views.edit_milestone, name='edit_milestone'),
    path('milestone/delete/<int:pk>', views.delete_material, name='delete_milestone'),
    
    ]