# Generated by Django 4.2.11 on 2024-05-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_books_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="notes",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
