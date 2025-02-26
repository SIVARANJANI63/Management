# Generated by Django 4.1.6 on 2024-02-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="default.webp",
                null=True,
                upload_to="images/profile/",
            ),
        ),
    ]
