# Generated by Django 2.2.5 on 2019-09-16 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_console'),
    ]

    operations = [
        migrations.RenameField(
            model_name='console',
            old_name='console',
            new_name='name',
        ),
    ]