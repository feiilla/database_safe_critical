# Generated by Django 4.2 on 2023-05-24 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0011_rename_mdescribtion_module_describtion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='ego_trajectory',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='report',
            name='objecter_trajectory',
        ),
    ]