# Generated by Django 3.1.6 on 2021-03-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='code',
        ),
        migrations.AddField(
            model_name='order',
            name='order_code',
            field=models.CharField(default='40gHyTui', editable=False, max_length=70),
        ),
        migrations.AddField(
            model_name='order',
            name='order_placed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='order_placed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='order_code',
            field=models.CharField(default='40gHyTui', editable=False, max_length=70),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='order_placed',
            field=models.BooleanField(default=False),
        ),
    ]