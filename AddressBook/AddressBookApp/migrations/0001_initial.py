# Generated by Django 2.0.6 on 2018-07-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressBookApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email_address', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField(max_length=20)),
                ('city', models.TextField(max_length=50)),
                ('state', models.TextField(max_length=50)),
                ('notes', models.TextField(max_length=200)),
            ],
        ),
    ]