# Generated by Django 5.1.5 on 2025-01-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0012_remove_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignedTo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]