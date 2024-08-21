from django.contrib import admin
from .models import Activity,  Employee, Project, Personnel, Machinery, Material, Milestone, Status
# Register your models here.
admin.site.register(Activity)
admin.site.register(Project)
admin.site.register(Personnel)
admin.site.register(Machinery)
admin.site.register(Material)
admin.site.register(Milestone)
admin.site.register(Employee)
admin.site.register(Status)