# Generated by Django 4.2 on 2023-05-04 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0008_report_scenename'),
    ]

    operations = [
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='scene',
            name='modules',
            field=models.ManyToManyField(blank=True, to='scenes.module'),
        ),
    ]
