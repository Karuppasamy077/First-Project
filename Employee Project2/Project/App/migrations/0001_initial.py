# Generated by Django 4.0.3 on 2022-03-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empname', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Salary', models.IntegerField()),
                ('Position', models.CharField(max_length=20)),
                ('Contact', models.IntegerField()),
                ('Address', models.CharField(max_length=30)),
            ],
        ),
    ]
