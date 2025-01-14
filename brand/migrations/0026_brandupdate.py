# Generated by Django 4.1.4 on 2023-01-31 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("brand", "0025_alter_brandfeature_offered_and_more")]

    operations = [
        migrations.CreateModel(
            name="BrandUpdate",
            fields=[
                (
                    "brand_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="brand.brand",
                    ),
                ),
                (
                    "additional_info",
                    models.TextField(
                        blank=True,
                        default="",
                        verbose_name="Add any additional information or explanation for this change",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, default="", max_length=254, verbose_name="Your email address"
                    ),
                ),
                (
                    "consent",
                    models.BooleanField(
                        default=False, verbose_name="Can we reach out to you via email?"
                    ),
                ),
                (
                    "update_tag",
                    models.CharField(
                        help_text=("the tag we use or this brand record at Bank.Green. ",),
                        max_length=100,
                    ),
                ),
            ],
            options={"abstract": False},
            bases=("brand.brand",),
        )
    ]
