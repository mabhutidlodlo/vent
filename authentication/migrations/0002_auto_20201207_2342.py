# Generated by Django 3.1.3 on 2020-12-07 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='djangoAvatar.jpg', upload_to='profile_pictures'),
        ),
    ]
