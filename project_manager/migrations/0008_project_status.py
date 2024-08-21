# Generated by Django 5.1 on 2024-08-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0007_activity_cost_unit_machinery_cost_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('comp', 'complete'), ('st', 'stalled'), ('in_prog', 'in_progress')], default='in_prog', max_length=100),
        ),
    ]
