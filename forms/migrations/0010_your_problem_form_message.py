# Generated by Django 5.0.6 on 2024-10-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_alter_volunteer_form_aadhar_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='your_problem_form',
            name='message',
            field=models.TextField(blank=True, default=None, max_length=4000, null=True),
        ),
    ]
