# Generated by Django 2.0.1 on 2018-01-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0009_auto_20180113_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='image',
            field=models.ImageField(blank=True, default='resources/default/lec_avatar.png', null=True, upload_to='resources/lec_avatars/'),
        ),
        migrations.AlterField(
            model_name='university',
            name='logo',
            field=models.ImageField(blank=True, default='resources/default/u_logo.png', null=True, upload_to='resources/u_logo/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, default='resources/default/user_ava.png', null=True, upload_to='resources/user_avatars/'),
        ),
    ]
