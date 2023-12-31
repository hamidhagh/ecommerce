# Generated by Django 4.2.3 on 2023-09-08 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_alter_order_amount_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.BigIntegerField(verbose_name='amount_paid'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 14, 34, 53, 382122, tzinfo=datetime.timezone.utc), verbose_name='datetime_created'),
        ),
    ]
