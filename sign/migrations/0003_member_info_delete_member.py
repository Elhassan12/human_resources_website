# Generated by Django 4.0.4 on 2022-05-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_rename_addmember_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('password', models.SlugField(max_length=20)),
                ('companyname', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]