# Generated by Django 2.0.3 on 2018-04-09 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0019_merge_20180408_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatus',
            name='can_moderate',
            field=models.BooleanField(default=False),
        ),
    ]
