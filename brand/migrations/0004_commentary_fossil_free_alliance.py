# Generated by Django 4.0.5 on 2022-06-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0003_remove_commentary_recommended_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='fossil_free_alliance',
            field=models.BooleanField(default=False, help_text='Is this brand in the fossil free alliance?'),
        ),
    ]
