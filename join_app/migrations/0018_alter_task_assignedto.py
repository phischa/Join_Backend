# Generated by Django 5.1.5 on 2025-01-20 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0017_alter_task_assignedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignedTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='join_app.contact'),
        ),
    ]
