# Generated by Django 5.1.5 on 2025-01-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0008_alter_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='color',
            field=models.CharField(default='#ACAFC1', max_length=25),
        ),
        migrations.AddField(
            model_name='contact',
            name='initials',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]