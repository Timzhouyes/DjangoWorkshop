# Generated by Django 2.2.3 on 2019-07-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='comment_id',
            field=models.IntegerField(null=True),
        ),
    ]