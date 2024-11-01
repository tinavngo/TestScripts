# Generated by Django 4.2.16 on 2024-10-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ingredients', models.CharField(help_text='Enter the ingredient, separated by comma', max_length=200)),
                ('cooking_time', models.PositiveIntegerField(help_text='Enter time in minutes')),
            ],
        ),
    ]