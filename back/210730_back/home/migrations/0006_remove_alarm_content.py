# Generated by Django 3.2.5 on 2021-07-28 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alarm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='content',
        ),
    ]