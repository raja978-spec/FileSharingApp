# Generated by Django 3.2.8 on 2023-03-04 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSharing', '0004_filemodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemodel',
            name='title',
        ),
    ]
