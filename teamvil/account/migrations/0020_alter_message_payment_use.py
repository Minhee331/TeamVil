# Generated by Django 3.2.5 on 2021-08-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_message_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_payment',
            name='use',
            field=models.IntegerField(default=1),
        ),
    ]
