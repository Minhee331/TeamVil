# Generated by Django 3.2.5 on 2021-07-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_view_cnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]