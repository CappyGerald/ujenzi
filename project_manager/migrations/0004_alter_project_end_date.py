# Generated by Django 5.1 on 2024-08-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0003_remove_personel_role_alter_personel_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
