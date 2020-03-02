# Generated by Django 2.0.6 on 2018-07-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddressBookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbookapplication',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='addressbookapplication',
            name='email_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='addressbookapplication',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='addressbookapplication',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
