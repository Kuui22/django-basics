# Generated by Django 5.0.6 on 2024-07-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stablexl", "0004_alter_post_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="img",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="image/"
            ),
        ),
    ]