# Generated by Django 3.1.2 on 2020-12-12 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_award'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='award',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='award',
            name='title',
        ),
    ]
