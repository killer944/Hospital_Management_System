# Generated by Django 3.1.6 on 2021-05-16 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_doctordata_specialist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='doctorlogin',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]