# Generated by Django 4.2.6 on 2023-11-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("back", "0010_orderitems_rename_user_id_customer_orders_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="img",
            field=models.ImageField(upload_to="htmls/static"),
        ),
    ]
