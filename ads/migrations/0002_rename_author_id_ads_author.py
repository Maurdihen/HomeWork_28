# Generated by Django 4.2.2 on 2023-06-16 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='author_id',
            new_name='author',
        ),
    ]