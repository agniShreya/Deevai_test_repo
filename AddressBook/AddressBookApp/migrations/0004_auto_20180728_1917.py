# Generated by Django 2.0.6 on 2018-07-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddressBookApp', '0003_auto_20180728_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbookapplication',
            name='phone_number',
            field=models.IntegerField(max_length=12),
        ),
    ]
