# Generated by Django 5.0.6 on 2024-12-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_footer_and_home_page_data_about_us_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='Image',
            field=models.URLField(default='https://drive.google.com/thumbnail?id=1eS5nP8cMj8eJ-Nq_PHTgLa7rJkj5UCPh&sz=s4000', max_length=3000),
        ),
    ]