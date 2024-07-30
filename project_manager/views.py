from django.shortcuts import render, get_object_or_404, redirect
from .models import Activity, Project, Personel, Machinery, Material, Milestone
from .forms import ProjectForm, MachineryForm, MaterialForm,\
    PersonelForm, ActivityForm, MilestoneForm

# Create your views here.
def home(request):
    return render(request, 'project_manager/home.html')
def activity_view(request):
    activities = Activity.objects.all()
    return render(request, 'project_manager/activity_view.html', {'activities': activities})

def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('activity_view')
    else:
        form = ActivityForm()
    return render(request, 'project_manager/add_activity_form.html', {'form': form})
def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            redirect('activity_view')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'edit_activity_form.html', {'form': form})

def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        redirect('activity_view')
    return render(request, 'delete_activity_form.html', {'activity': activity})

def project_view(request):
    projects = Project.objects.all()
    return render(request,
                  'project_manager/project_view.html',
                  {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('project_view')
    else:
        form = ProjectForm()
    return render(request, 'project_manager/add_project_form.html', {'form':form})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        redirect('project_view')
    return render(request, 'project_manager/delete_project_form.html', {'project': project})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project) 
        if form.is_valid():
            form.save()
            redirect('project_manager/project_detail_view', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_manager/edit_project_form.html', {'form': form, 'project': project})

def machinery_view(request):
    machineries = Machinery.objects.all()
    return render(request,
                  'project_manager/machinery_form.html',
                  {'machineries': machineries})

def add_machinery(request):
    if request.method == 'POSt':
        form = MachineryForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('machinery_iew')
    else:
        form = MachineryForm()
    return render(request,
                  'project_manager/add_machinery.html',
                  {'form': form})
def edit_machinery(request, pk):
    machinery = get_list_or_404(Machinery,
                                pk=pk)
    if request.method == 'POST':
        form = MachineryForm(request.POST, instance=machinery)
        if form.is_valid():
            form.save()
            redirect('machinery_view')
    else:
        form = MachineryForm(instance=machinery)
    return render(request,
                  'project_manager/edit_machinery.html',
                  {'form':form})
def delete_machinery(request, pk):
    machinery = get_object_or_404(Machinery,
                                pk=pk)
    if request.method == 'POST':
        machinery.delete()
        redirect('machinery_view')
    return render(request, 'project_manager/delete_machinery.html', {'machinery': machinery})

def material_view(request):
    materials = Material.objects.all()
    return render (request, 'project_manager/material_view.html', {'materials': materials})

def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('material_view')
    else:
        form = MaterialForm()
    return render(request, 'project_manager/add_material.html', {'form': form})

def edit_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            redirect('material_iew')
    else:
        
        form = MachineryForm(instance=material)
    return render(request, 'project_manager/edit_material_form.html', {'form': form})

def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        redirect('material_view')
    return render(request, 'project_manager/delete_material.html', {'material': material})

def personel_view(request):
    personel = Personel.objects.all()
    return render(request, 'project_manager/personel_view.html', {'personel': personel})

def add_personel(request):
    if request.method == 'POST':
        form = PersonelForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            redirect('personel_view')
        else:
            print('form is invalid!')
            print(form.errors)
    else:
        form = PersonelForm()
    return render(request, 'project_manager/add_personel.html', {'form': form})

def edit_personel(request, pk):
    personel = get_object_or_404(Personel, pk=pk)
    if request.method == 'POST':
        form = PersonelForm(request.POST, instance=personel)
        if form.is_valid():
            form.save()
            redirect('personel_view')
    else:
        form = PersonelForm(instance=personel)
    return render(request, 'project_manager/edit_personel_form.html', {'form': form})

def delete_personel(request, pk):
    personel = get_object_or_404(Personel, pk=pk)
    if request.method == 'POST':
        personel.delete()
        redirect('personel_view')
    return render(request, 'project_manager/delete_personel_form.html', {'personel': personel})

def milestone_view(request):
    milestones =  Milestone.objects.all()
    return render(request, 'project_manager/milestone_view.html', {'milestones':milestones})

def add_milestone(request):
    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('milestone_view')
    else:
        form = MilestoneForm()
    return render(request, 'project_manager/add_milestone_form.html', {'form': form})

def edit_milestone(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk)
    if request.method == 'POST':
        form = MilestoneForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            redirect('milestone_view')
    else:
        form = MilestoneForm(instance=milestone)
    return render(request, 'project_manager/edit_milestone_form.html', {'form': form})

def delete_milestone(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk)
    if request.method == 'POST':
        milestone.delete()
        redirect('milestone_view')
    return render(request, 'project_manager/delete_milestone_form.html', {'milestone': milestone})