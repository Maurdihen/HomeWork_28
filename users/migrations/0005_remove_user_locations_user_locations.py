# Generated by Django 4.2.2 on 2023-06-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_location_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='locations',
        ),
        migrations.AddField(
            model_name='user',
            name='locations',
            field=models.ManyToManyField(to='users.location'),
        ),
    ]
