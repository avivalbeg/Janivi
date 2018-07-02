# Generated by Django 2.0.6 on 2018-07-02 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('notebook_location', models.CharField(max_length=1000)),
                ('notebook_description', models.CharField(max_length=500)),
            ],
        ),
    ]
