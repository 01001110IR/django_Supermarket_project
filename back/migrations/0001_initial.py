# Generated by Django 4.2.6 on 2023-10-31 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, null=True)),
                ("mail", models.EmailField(max_length=255, null=True)),
                ("address", models.CharField(max_length=255, null=True)),
                ("phone_number", models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("price", models.FloatField()),
                (
                    "img",
                    models.ImageField(
                        height_field="img_height",
                        upload_to="product_images/",
                        width_field="img_width",
                    ),
                ),
                ("img_width", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="back.category",
                    ),
                ),
            ],
        ),
    ]
