# Generated by Django 3.0.3 on 2020-03-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
