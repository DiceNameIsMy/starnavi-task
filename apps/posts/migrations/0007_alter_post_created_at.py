# Generated by Django 3.2.6 on 2021-08-13 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_updated_ad_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
