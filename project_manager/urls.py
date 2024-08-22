from django.urls import path
from . import views

app_name = 'project_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.project_view, name='project_view'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/delete/<int:pk>', views.delete_project, name='delete_project'),
    path('projects/edit/<int:pk>', views.edit_project, name='edit_project'),
    path('projects/detail/<int:pk>', views.project_detail, name='project_detail'),
    path('machinery/', views.machinery_view, name='machinery_view'),
    path('machinery/add/', views.add_machinery, name='add_machinery'),
    path('machinery/edit/<int:pk>', views.edit_machinery, name='edit_machinery'),
    path('machinery/detail/<int:pk>', views.machinery_detail, name='machinery_detail'),
    path('machinery/delete/<int:pk>', views.delete_machinery, name='delete_machinery'),
    path('materials/',views.material_view, name='material_view'),
    path('materials/detail/<int:pk>', views.material_detail, name='material_detail'),
    path('materials/add/', views.add_material, name='add_material'),
    path('materials/edit/<int:pk>', views.edit_material, name='edit_material'),
    path('materials/delete/<int:pk>', views.delete_material, name='delete_material'),
    path('activity', views.activity_view, name='activity_view'),
    path('activity/add/', views.add_activity, name='add_activity'),
    path('activity/detail/<int:pk>', views.activity_detail, name='activity_detail'),
    path('activity/edit/<int:pk>', views.edit_activity, name='edit_activity'),
    path('activity/delete/<int:pk>', views.delete_activity, name='delete_activity'),
    path('milestone/', views.milestone_view, name='milestone_view'),
    path('milestone/add/', views.add_milestone, name='add_milestone'),
    path('milestone/detail/<int:pk>', views.milestone_detail, name='milestone_detail'),
    path('milestone/edit/<int:pk>', views.edit_milestone, name='edit_milestone'),
    path('milestone/delete/<int:pk>', views.delete_material, name='delete_milestone'),
    path('employee/', views.employee_view, name='employee_view'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('employee/edit/<int:pk>', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:pk>', views.delete_employee, name='delete_employee'),
    
    ]