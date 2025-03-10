# Generated by Django 5.1.7 on 2025-03-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_id_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Overdue', 'Overdue')], editable=False, max_length=20),
        ),
    ]
