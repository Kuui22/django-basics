# Generated by Django 5.0.6 on 2024-07-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stablexl", "0003_alter_post_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="img",
            field=models.FileField(
                blank=True, default=None, null=True, upload_to="image/"
            ),
        ),
    ]