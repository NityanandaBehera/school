# Generated by Django 4.0.3 on 2022-03-30 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_stud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud',
            old_name='stu_adddress',
            new_name='stu_address',
        ),
    ]