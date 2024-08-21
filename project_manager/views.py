from django.shortcuts import render, get_object_or_404, redirect
from .models import Activity, Employee,Project, Personnel, Machinery, Material, Milestone
from .forms import  EmployeeForm, ProjectForm, MachineryForm, MaterialForm,\
    PersonnelForm, ActivityForm, MilestoneForm
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'project_manager/base.html', {'show_image': True})
@login_required
def dashboard(request):
    return render(request, 'project_manager/dashboard.html', {'current_year': datetime.now().year, 'show_image': False})

@login_required
def activity_view(request):
    activities = Activity.objects.all().order_by('id')
    paginator = Paginator(activities, 3)
    page_number = request.GET.get('page', 1)
    try:
        activities_list = paginator.page(page_number)
    except EmptyPage:
        activities_list = paginator.page(paginator.num_pages)
   
    return render(request, 'project_manager/activity_view.html', {'activities': activities, 'show_image': False})

@login_required
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'project_manager/activity_detail.html', {'activity': activity, 'show_image': False})

@login_required
def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_manager:activity_view')
    else:
        form = ActivityForm()
    return render(request, 'project_manager/add_activity_form.html', {'form': form, 'show_image': False})

@login_required
def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('project_manager:activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'project_manager/edit_activity_form.html', {'form': form, 'show_image': False})

@login_required
def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('project_manager:activity_view')
    return render(request, 'delete_activity_form.html', {'activity': activity, 'show_image': False})

@login_required
def employee_view(request):
    employees = Employee.objects.all().order_by('id')
    paginator = Paginator(employees, 3)
    page_number = request.GET.get('page', 1)
    try:
        employee_list = paginator.page(page_number)
    except EmptyPage:
        employee_list = paginator.page(paginator.num_pages)
   
    return render(request, 'project_manager/employee_view.html', {'employees': employees, 'show_image': False})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'project_manager/employee_detail.html', {'employee': employee, 'show_image': False})

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm()
        if form.is_valid():
            form.save()
            return redirect('project_manager:employee_view')
    else:
        form = EmployeeForm()
    return render(request, 'project_manager/add_employee.html', {'form':form, 'show_image': False})

@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('project_manager:employee_detail')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'project_manager/edit_employee.html', {'form': form, 'show_image': False})

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('project_manager:employee_view')
    return render(request, 'project_manager/delete_employee.html', {'employee': employee, 'show_image': False})
    
@login_required
def project_view(request):
    projects = Project.objects.all().order_by('id')
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page', 1)
    try:
        project_list = paginator.page(page_number)
    except EmptyPage:
        project_list = paginator.page(paginator.num_pages)
    return render(request,
                  'project_manager/project_view.html',
                  {'projects': projects, 'show_image':False})
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_manager/project_detail.html', {'project': project})
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_manager:project_view')
    else:
        form = ProjectForm()
    print(form.fields)
    return render(request, 'project_manager/add_project_form.html', {'form':form, 'show_image': False})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_manager:project_view')
    return render(request, 'project_manager/delete_project_form.html', {'project': project, 'show_image': False})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project) 
        if form.is_valid():
            form.save()
            return redirect('project_manager:project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_manager/edit_project_form.html', {'form': form, 'project': project,' show_image': False })

@login_required
def machinery_view(request):
    machineries = Machinery.objects.all().order_by('id')
    paginator = Paginator(machineries, 3)
    page_number = request.GET.get('page', 1)
    try:
        machinery_list = paginator.page(page_number)
    except EmptyPage:
        machinery_list = paginator.page(paginator.num_pages)
    return render(request,
                  'project_manager/machinery_form.html',
                  {'machineries': machineries})

@login_required
def machinery_detail(request, pk):
    machinery = get_object_or_404(Machinery, pk=pk)
    return render(request,  'project_manager/machinery_detail.html', {'machinery': machinery,'show_image': False })

@login_required
def add_machinery(request):
    if request.method == 'POST':
        form = MachineryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_manager:machinery_view')
    else:
        form = MachineryForm()
    return render(request,
                  'project_manager/add_machinery.html',
                  {'form': form, 'show_image': False})

@login_required
def edit_machinery(request, pk):
    machinery = get_object_or_404(Machinery,
                                pk=pk)
    if request.method == 'POST':
        form = MachineryForm(request.POST, instance=machinery)
        if form.is_valid():
            form.save()
            return redirect('project_manager:machinery_detail', pk=machinery.pk)
    else:
        form = MachineryForm(instance=machinery)
    return render(request,
                  'project_manager/edit_machinery.html',
                  {'form':form, 'show_image': False})

@login_required
def delete_machinery(request, pk):
    machinery = get_object_or_404(Machinery,
                                pk=pk)
    if request.method == 'POST':
        machinery.delete()
        return redirect('project_manager:machinery_view')
    return render(request, 'project_manager/delete_machinery.html', {'machinery': machinery, 'show_image': False})

@login_required
def material_view(request):
    materials = Material.objects.all().order_by('id')
    paginator = Paginator(materials, 3)
    page_number = request.GET.get('page', 1)
    try:
        material_list = paginator.page(page_number)
    except EmptyPage:
        material_list = paginator.page(paginator.num_pages)
    return render (request, 'project_manager/material_view.html', {'materials': materials, 'show_image': False})

@login_required
def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)
    return render(request, 'project_manager/material_detail.html',
                  {'material': material, 'show_image': False})
@login_required
def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_manager:material_view')
    else:
        form = MaterialForm()
    return render(request, 'project_manager/add_material.html', {'form': form, 'show_image': False})

@login_required
def edit_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('project_manager:material_detail', pk=material.pk)
    else:
        
        form = MaterialForm(instance=material)
    return render(request, 'project_manager/edit_material_form.html', {'form': form, 'show_image': False})

@login_required
def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('project_manager:material_view')
    return render(request, 'project_manager/delete_material.html', {'material': material, 'show_image': False})

@login_required
def personnel_view(request):
    personnel = Personnel.objects.all().order_by('id')
    paginator = Paginator(personnel, 3)
    page_number = request.GET.get('page', 1)
    try:
        page_obj  = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'project_manager/personnel_view.html', {'page_obj': page_obj, 'show_image': False})

@login_required
def personnel_detail(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    return render(request, 'project_manager/personnel_detail.html', {'personel': personnel, 'show_image': False})

@login_required
def add_personnel(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('project_manager:personnel_view')
        else:
            print('form is invalid!')
            print(form.errors)
    else:
        form = PersonnelForm()
    return render(request, 'project_manager/add_personnel.html', {'form': form, 'show_iamge': False})

@login_required
def edit_personnel(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('project_manager:personnel_detail', pk=personnel.pk)
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'project_manager/edit_personnel_form.html', {'form': form, 'show_image': False})

@login_required
def delete_personnel(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        personnel.delete()
        return redirect('project_manager:personnel_view')
    return render(request, 'project_manager/delete_personnel_form.html', {'personel': personnel, 'show_image': False})

@login_required
def milestone_view(request):
    milestones =  Milestone.objects.all()
    paginator = Paginator(milestones, 3)
    page_number = request.GET.get('page', 1)
    try:
        milestone_list = paginator.page(page_number)
    except EmptyPage:
        milestone_list = paginator.page(paginator.num_pages)
    return render(request, 'project_manager/milestone_view.html', {'milestones':milestones, 'show_image': False})

@login_required
def milestone_detail(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk)
    return render(request, 'project_manager/milestone_detail.html', {'milestone': milestone, 'show_image': False})

@login_required
def add_milestone(request):
    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_manager:milestone_view')
    else:
        form = MilestoneForm()
    return render(request, 'project_manager/add_milestone_form.html', {'form': form, 'show_image': False})

@login_required
def edit_milestone(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk)
    if request.method == 'POST':
        form = MilestoneForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('project_manager:milestone_detail', pk=milestone.pk)
    else:
        form = MilestoneForm(instance=milestone)
    return render(request, 'project_manager/edit_milestone_form.html', {'form': form, 'show_image': False})

@login_required
def delete_milestone(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk)
    if request.method == 'POST':
        milestone.delete()
        redirect('project_manager:milestone_view')
    return render(request, 'project_manager/delete_milestone_form.html', {'milestone': milestone, 'show_image': False})