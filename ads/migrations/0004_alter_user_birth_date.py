# Generated by Django 4.1.6 on 2023-02-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_category_slug_user_birth_date_alter_ad_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
