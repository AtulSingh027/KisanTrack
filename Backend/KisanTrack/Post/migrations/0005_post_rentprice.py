# Generated by Django 5.1.5 on 2025-02-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_remove_post_category_remove_post_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='RentPrice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
