# Generated by Django 2.0.6 on 2018-07-02 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Geography_Notebooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='notebook_date_added',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
