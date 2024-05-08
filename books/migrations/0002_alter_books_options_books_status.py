# Generated by Django 4.2.11 on 2024-05-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="books",
            options={"verbose_name_plural": "Books"},
        ),
        migrations.AddField(
            model_name="books",
            name="status",
            field=models.CharField(
                choices=[
                    ("library", "Library"),
                    ("reading", "Currently Reading"),
                    ("completed", "Completed"),
                ],
                default="library",
                max_length=20,
            ),
        ),
    ]
