# Generated by Django 2.0.3 on 2018-04-09 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0020_userstatus_can_moderate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatus',
            name='can_publish_without_moderation',
            field=models.BooleanField(default=False),
        ),
    ]
