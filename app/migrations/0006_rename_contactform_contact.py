# Generated by Django 4.1.6 on 2023-02-13 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contactform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Contact',
        ),
    ]
