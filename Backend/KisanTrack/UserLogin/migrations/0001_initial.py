# Generated by Django 5.1.5 on 2025-02-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('Pic', models.ImageField(blank=True, upload_to='images/UserProfilePic/')),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
