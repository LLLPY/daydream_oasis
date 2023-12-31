# Generated by Django 4.1.5 on 2023-04-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0009_alter_tag_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(
                blank=True,
                db_column="标题",
                help_text="标题",
                max_length=8,
                unique=True,
                verbose_name="标题",
            ),
        ),
    ]
