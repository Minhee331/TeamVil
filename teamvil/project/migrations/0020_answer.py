# Generated by Django 3.2.5 on 2021-07-23 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_apply_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('choice_answer', models.IntegerField(null=True)),
                ('choice_text', models.CharField(max_length=100, null=True)),
                ('short_answer', models.CharField(max_length=100, null=True)),
                ('long_answer', models.TextField(null=True)),
                ('question_id', models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='project.question')),
            ],
        ),
    ]
