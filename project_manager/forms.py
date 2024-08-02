from django.forms import ModelForm
from .models import Activity, Project, Personel,Machinery, Material, Milestone

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'budget', 'start_date', 'end_date', 'expected_revenue', 'revenue_unit']

class MachineryForm(ModelForm):
    class Meta:
        model = Machinery
        fields = ['project','name', 'machine_type', 'num_of_machines', 'cost']

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['project','name', 'quantity', 'quantity_units', 'cost' ]

class PersonelForm(ModelForm):
    class Meta:
        model = Personel
        fields = ['project','user', 'role','join_date', 'end_date']

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['project', 'name', 'description', 'start_date', 'end_date', 'cost' ]

class MilestoneForm(ModelForm):
    class Meta:
        model = Milestone
        fields = ['project','name', 'distance', 'distance_units']

