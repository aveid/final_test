# Generated by Django 4.1.5 on 2023-01-23 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                ("price", models.PositiveIntegerField()),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "на складе есть"),
                            (2, "на складе нет"),
                            (3, "под заказ"),
                        ]
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test.category",
                    ),
                ),
            ],
        ),
    ]
