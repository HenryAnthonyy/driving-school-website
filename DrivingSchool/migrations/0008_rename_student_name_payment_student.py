# Generated by Django 4.0.2 on 2022-02-18 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DrivingSchool', '0007_rename_student_name_enrollment_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='student_name',
            new_name='student',
        ),
    ]
