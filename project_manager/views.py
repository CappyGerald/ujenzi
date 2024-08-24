
from .models import Activity, Employee,Project, Machinery, Material, Milestone
from .forms import  EmployeeForm, ProjectForm, MachineryForm, MaterialForm, ActivityForm, MilestoneForm
from django.core.paginator import Paginator, EmptyPage
# from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime

# Create your views here.
class IndexView(TemplateView):
    template_name = 'project_manager/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = True
        return context

class DashboardView(TemplateView):
    template_name = 'project_manager/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_year'] = datetime.now().year
        context['show_image'] = False
        return context
    
class ActivityListiew(ListView):
    model = Activity
    template_name = 'project_manager/activity_view.html'
    context_objct_name = 'activities'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['show_image'] = False
        return context
    
class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'project_manager/activity_detail.html'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'project_manager/add_activity.html'
    success_url = reverse_lazy('project_manager:activity_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = True
        return context
    
class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'project_manager/edit_activity.html'

    def get_success_url(self) -> str:
        return reverse_lazy('project_manager:activity_detail', kwargs={'pk':self.object.pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class DeleteActivityView(DeleteView):
    model = Activity
    template_name = 'project_manager/delete_activity.html'
    success_url = reverse_lazy('project_manager:activity_view')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context

    
class EmployeeListiew(ListView):
    model = Employee
    template_name = 'project_manager/employee_view.html'
    context_objct_name = 'employees'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['show_image'] = True
        return context
    
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'project_manager/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'project_manager/add_employee.html'
    success_url = reverse_lazy('project_manager:employee_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class EmployeeUpdateView(UpdateView):
    model = EmployeeForm
    form_class = EmployeeForm
    template_name = 'project_manager/edit_employee.html'

    def get_success_url(self) -> str:
        return reverse_lazy('project_manager:employee_detail', kwargs={'pk':self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class DeleteEmployeeView(DeleteView): 
    model = Employee
    template_name = 'project_manager/delete_employee.html'
    success_url = reverse_lazy('project_manager:employee_view')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context

class MilestoneListiew(ListView):
    model = Milestone
    template_name = 'project_manager/milestone_view.html'
    context_objct_name = 'milestones'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['show_image'] = True
        return context
    
class MilestoneDetailView(DetailView):
    model = Milestone
    template_name = 'project_manager/milestone_detail.html'
    context_object_name = 'milestone'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context

   
class MilestoneCreateView(CreateView):
    model = Milestone
    form_class = MilestoneForm
    template_name = 'project_manager/add_milestone_form.html'
    success_url = reverse_lazy('project_manager:milestone_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class MilestoneUpdateView(UpdateView):
    model = Milestone
    form_class = EmployeeForm
    template_name = 'project_manager/edit_milesone_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('project_manager:milestone_detail', kwargs={'pk':self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class DeleteMilestoneView(DeleteView): 
    model = Milestone
    template_name = 'project_manager/delete_milestone_form.html'
    success_url = reverse_lazy('project_manager:milestone_view')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context

class MachineryListiew(ListView):
    model = Machinery
    template_name = 'project_manager/machinery_view.html'
    context_objct_name = 'machineries'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['show_image'] = True
        return context
    
class MachineryDetailView(DetailView):
    model = Machinery
    template_name = 'project_manager/machinery_detail.html'
    context_object_name = 'machinery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class MachineryCreateView(CreateView):
    model = Machinery
    form_class = MilestoneForm
    template_name = 'project_manager/add_machinery.html'
    success_url = reverse_lazy('project_manager:machinery_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class MachineryUpdateView(UpdateView):
    model = Machinery
    form_class = MachineryForm
    template_name = 'project_manager/edit_machinery.html'

    def get_success_url(self) -> str:
        return reverse_lazy('project_manager:machinery_detail', kwargs={'pk':self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class DeleteMachineryView(DeleteView): 
    model = Machinery
    template_name = 'project_manager/delete_machinery.html'
    success_url = reverse_lazy('project_manager:machinery_view')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context


class MaterialListiew(ListView):
    model = Material
    template_name = 'project_manager/material_view.html'
    context_objct_name = 'materials'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['show_image'] = True
        return context

class MaterialDetailView(DetailView):
    model = Project
    template_name = 'project_manager/material_detail.html'
    context_object_name = 'material'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context  
    
class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'project_manager/add_material.html'
    success_url = reverse_lazy('project_manager:material_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'project_manager/edit_material.html'

    def get_success_url(self) -> str:
        return reverse_lazy('project_manager:machinery_detail', kwargs={'pk':self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class DeleteMaterialtView(DeleteView): 
    model = Material
    template_name = 'project_manager/delete_material.html'
    success_url = reverse_lazy('project_manager:material_view')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context

class ProjectListiew(ListView):
    model = Project
    template_name = 'project_manager/project_view.html'
    context_objct_name = 'projects'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['show_image'] = True
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_manager/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_manager/add_project.html'
    success_url = reverse_lazy('project_manager:project_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_manager/edit_project.html'

    def get_success_url(self) -> str:
        return reverse_lazy('project_manager:machinery_detail', kwargs={'pk':self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
    
class DeleteProjectView(DeleteView): 
    model = Project
    template_name = 'project_manager/delete_project.html'
    success_url = reverse_lazy('project_manager:project_view')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_image'] = False
        return context
