# Generated by Django 2.2.7 on 2019-11-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=500)),
                ('course', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('gtname', models.CharField(max_length=500)),
            ],
        ),
    ]