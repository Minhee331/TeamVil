# Generated by Django 3.2.5 on 2021-07-13 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0007_auto_20210713_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='from_user_id',
            field=models.ForeignKey(db_column='from_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='review_from_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_review',
            name='to_user_id',
            field=models.ForeignKey(db_column='to_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='review_to_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]