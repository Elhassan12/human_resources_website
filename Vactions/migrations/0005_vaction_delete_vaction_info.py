# Generated by Django 4.0.4 on 2022-05-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vactions', '0004_vaction_info_delete_vaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaction',
            fields=[
                ('emp_id', models.TextField(max_length=5, primary_key=True, serialize=False)),
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
