# Generated by Django 4.1.7 on 2023-05-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("brand", "0031_alter_commentary_rating")]

    operations = [
        migrations.AddField(
            model_name="institutioncredential",
            name="prismic_api_id",
            field=models.CharField(
                blank=True,
                help_text="the associated prismic API ID. Must match perfectly with the SFIDefaults type related image field. e.g. institution_credentials-gabv'",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="from_the_website",
            field=models.TextField(
                blank=True,
                help_text="Deprecated. Text is not used in new SFI pages unless no other text is specified in prismic.",
            ),
        ),
    ]