from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    budget_unit = models.CharField(max_length=10, default='$')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    expected_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    revenue_unit = models.CharField(max_length=10, default='$')


    def __str__(self):
        return self.name
    
class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    department = models.CharField(max_length=250)
    position = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Personnel(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='personel')
    employee = models.ForeignKey(Employee,
                             on_delete=models.CASCADE, related_name='personel',
                             blank=True, null=True)
    join_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee} joined this project on {self.join_date}"

class Activity(models.Model):
    project = models.ForeignKey(Project,
                                related_name='activity',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    cost_unit = models.CharField(max_length=10, default='$')

    def __str__(self):
        return self.name
    
class Machinery(models.Model):
    project = models.ForeignKey(Project,
                                related_name='machinery',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    machine_type = models.CharField(max_length=250)
    num_of_machines = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    cost_unit = models.CharField(max_length=10, default='$')

    def __str__(self):
        return self.name


class Material(models.Model):
    project = models.ForeignKey(Project,
                                related_name='material',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    quantity_units = models.CharField(max_length=10, default='KG')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    cost_unit = models.CharField(max_length=10, default='$')

    def __str__(self):
        return self.name
    
class Milestone(models.Model):
    project = models.ForeignKey(Project,
                                related_name='milestone', 
                                on_delete=models.CASCADE,
                                default=1)
    name = models.CharField(max_length=250)
    distance  = models.CharField(max_length=250)
    distance_units = models.CharField(max_length=10, default='KM')