# Generated by Django 5.1.4 on 2025-01-11 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payments",
            options={
                "ordering": ["user", "pay_date", "payment_method"],
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платеж",
            },
        ),
    ]