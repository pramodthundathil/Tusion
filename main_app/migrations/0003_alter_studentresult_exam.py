# Generated by Django 5.0.2 on 2024-02-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_admin_id_alter_attendance_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='exam',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
