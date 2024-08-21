
from django.forms import ModelForm
from .models import Activity,Employee, Project, Personnel,Machinery, Material, Milestone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='post'
        self.helper.add_input(Submit('submit', 'save'))

    class Meta:
        model = Project
        fields = ['name', 'description', 'budget', 'start_date', 'end_date', 'expected_revenue', 'revenue_unit']

class MachineryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='post'
        self.helper.add_input(Submit('submit', 'save'))
    class Meta:
        model = Machinery
        fields = ['project','name', 'machine_type', 'num_of_machines', 'cost', 'cost_unit']

class MaterialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='post'
        self.helper.add_input(Submit('submit', 'save'))
    class Meta:
        model = Material
        fields = ['project','name', 'quantity', 'quantity_units', 'cost', 'cost_unit' ]

class PersonnelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='post'
        self.helper.add_input(Submit('submit', 'save'))
    class Meta:
        model = Personnel
        fields = ['project','employee','join_date', 'end_date']

class ActivityForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='post'
        self.helper.add_input(Submit('submit', 'save'))
    class Meta:
        model = Activity
        fields = ['project', 'name', 'description', 'start_date', 'end_date', 'cost', 'cost_unit' ]

class MilestoneForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='post'
        self.helper.add_input(Submit('submit', 'save'))
    class Meta:
        model = Milestone
        fields = ['project','name', 'distance', 'distance_units']

class EmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='post'
        self.helper.add_input(Submit('submit', 'save'))
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'department', 'position']

