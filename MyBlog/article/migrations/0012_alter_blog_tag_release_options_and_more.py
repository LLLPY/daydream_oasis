# Generated by Django 4.1.5 on 2023-04-16 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0011_blog_tag_release"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog_tag_release",
            options={"verbose_name": "博客_标签关系表", "verbose_name_plural": "博客_标签关系表"},
        ),
        migrations.AlterModelTable(
            name="blog_tag_release",
            table="博客_标签关系表",
        ),
    ]
