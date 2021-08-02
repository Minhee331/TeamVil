# Generated by Django 3.2.5 on 2021-07-16 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_project_education_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='isEnd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='isFile',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='isLink',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='mem_duty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='school',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='use',
            field=models.IntegerField(default=0),
        ),
    ]
