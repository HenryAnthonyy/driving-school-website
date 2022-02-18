# Generated by Django 4.0.2 on 2022-02-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DrivingSchool', '0003_schedule_instuctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='instuctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DrivingSchool.instructor'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='schedule_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DrivingSchool.schedule'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DrivingSchool.student'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DrivingSchool.student'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
