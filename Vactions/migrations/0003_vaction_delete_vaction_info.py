# Generated by Django 4.0.4 on 2022-05-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vactions', '0002_vaction_info_delete_vaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20)),
                ('ft_name', models.TextField(max_length=20)),
                ('lt_name', models.TextField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_days', models.IntegerField()),
                ('reason', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Vaction_info',
        ),
    ]
