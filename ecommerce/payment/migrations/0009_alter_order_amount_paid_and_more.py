# Generated by Django 4.2.3 on 2023-09-08 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_alter_order_amount_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.BigIntegerField(default=1, verbose_name='amount_paid'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 14, 38, 0, 805156, tzinfo=datetime.timezone.utc), verbose_name='datetime_created'),
        ),
    ]
