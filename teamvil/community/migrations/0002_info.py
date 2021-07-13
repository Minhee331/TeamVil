# Generated by Django 3.2.5 on 2021-07-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('write_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('content', models.TextField()),
                ('isLink', models.IntegerField()),
                ('isFile', models.IntegerField()),
                ('view_cnt', models.IntegerField(default=0)),
            ],
        ),
    ]
