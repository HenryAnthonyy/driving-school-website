# Generated by Django 4.0.2 on 2022-02-19 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DrivingSchool', '0009_rename_name_instructor_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='Firstname',
            new_name='name',
        ),
    ]