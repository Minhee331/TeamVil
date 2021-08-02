# Generated by Django 3.2.4 on 2021-07-01 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mbti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbti', models.CharField(max_length=4)),
                ('mbti_cnt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20)),
                ('term_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_carrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=45)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('content', models.TextField()),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mbti_detail', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('openPhone', models.IntegerField()),
                ('openEmail', models.IntegerField()),
                ('field2', models.CharField(max_length=20)),
                ('state', models.IntegerField()),
                ('isLink', models.IntegerField()),
                ('isFile', models.IntegerField()),
                ('isCarrer', models.IntegerField()),
                ('pr', models.TextField(null=True)),
                ('register', models.DateTimeField()),
                ('photo', models.CharField(max_length=100)),
                ('isReview', models.IntegerField()),
                ('view_cnt', models.IntegerField()),
                ('education_id', models.ForeignKey(db_column='education_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.education')),
                ('field1_id', models.ForeignKey(db_column='field1_id', on_delete=django.db.models.deletion.CASCADE, to='home.field1')),
                ('job_id', models.ForeignKey(db_column='job_id', on_delete=django.db.models.deletion.CASCADE, to='account.job')),
                ('mbti_id', models.ForeignKey(db_column='mbti_id', on_delete=django.db.models.deletion.CASCADE, to='account.mbti')),
                ('region1_id', models.ForeignKey(db_column='region1_id', on_delete=django.db.models.deletion.CASCADE, to='home.region1')),
                ('region2_id', models.ForeignKey(db_column='region2_id', on_delete=django.db.models.deletion.CASCADE, to='home.region2')),
                ('term_id', models.ForeignKey(db_column='term_id', on_delete=django.db.models.deletion.CASCADE, to='account.term')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
