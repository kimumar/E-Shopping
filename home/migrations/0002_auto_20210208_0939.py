# Generated by Django 3.1.6 on 2021-02-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='about',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contact',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='setting',
            name='refrences',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
