# Generated by Django 3.2.6 on 2021-11-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0014_alter_user_following'),
        ('images', '0002_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
