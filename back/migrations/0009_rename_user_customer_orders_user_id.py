# Generated by Django 4.2.6 on 2023-11-06 20:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("back", "0008_orderdetails_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer_orders",
            old_name="user",
            new_name="user_id",
        ),
    ]
