# Generated by Django 4.0.2 on 2022-02-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrivingSchool', '0004_enrollment_instuctor_alter_enrollment_schedule_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='instuctor',
            new_name='instructor',
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]