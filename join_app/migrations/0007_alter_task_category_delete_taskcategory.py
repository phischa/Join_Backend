# Generated by Django 5.1.5 on 2025-01-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0006_taskcategory_rename_assigned_task_assignedto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('technicalTask', 'technicalTask'), ('userStory', 'userStory'), ('bug', 'bug'), ('feature', 'feature'), ('refactor"', 'refactor'), ('documentation', 'documentation'), ('doTestingne', 'Testing'), ('Analysis', 'Analysis'), ('Design', 'Design'), ('No Category', 'No Category')], max_length=30),
        ),
        migrations.DeleteModel(
            name='TaskCategory',
        ),
    ]
