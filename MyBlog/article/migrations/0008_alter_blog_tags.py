# Generated by Django 4.1.5 on 2023-04-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0007_alter_category_time_alter_collection_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="tags",
            field=models.ManyToManyField(
                db_column="标签",
                help_text="标签",
                related_name="blogs",
                to="article.tag",
                verbose_name="标签",
            ),
        ),
    ]
