# Generated by Django 4.1.5 on 2023-04-10 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0006_blog_recommendation_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="time",
            field=models.DateTimeField(
                db_column="创建时间",
                default=datetime.datetime.now,
                help_text="创建时间",
                verbose_name="创建时间",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="time",
            field=models.DateTimeField(
                db_column="收藏日期",
                default=datetime.datetime.now,
                help_text="收藏日期",
                verbose_name="收藏日期",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(
                db_column="评论时间",
                default=datetime.datetime.now,
                help_text="评论时间",
                verbose_name="评论时间",
            ),
        ),
        migrations.AlterField(
            model_name="like",
            name="time",
            field=models.DateTimeField(
                db_column="点赞时间",
                default=datetime.datetime.now,
                help_text="点赞时间",
                verbose_name="点赞时间",
            ),
        ),
        migrations.AlterField(
            model_name="search",
            name="time",
            field=models.DateTimeField(
                db_column="时间",
                default=datetime.datetime.now,
                help_text="时间",
                verbose_name="时间",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="time",
            field=models.DateTimeField(
                db_column="创建时间",
                default=datetime.datetime.now,
                help_text="创建时间",
                verbose_name="创建时间",
            ),
        ),
    ]
