# Generated by Django 2.2.2 on 2021-01-04 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completeds',
            new_name='completed',
        ),
    ]
