# Generated by Django 4.1.5 on 2023-09-13 19:18

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('title', models.CharField(blank=True, help_text='标题', max_length=30, verbose_name='标题')),
                ('avatar', models.URLField(default='image/default_blog_avatar.jpg', help_text='封面', verbose_name='封面')),
                ('abstract', models.TextField(help_text='摘要', max_length=150, verbose_name='摘要')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(help_text='文章内容', verbose_name='文章内容')),
                ('dpv', models.PositiveIntegerField(default=0, help_text='dpv', verbose_name='dpv')),
                ('duv', models.PositiveIntegerField(default=0, help_text='duv', verbose_name='duv')),
                ('pv', models.PositiveIntegerField(default=0, help_text='pv', verbose_name='pv')),
                ('uv', models.PositiveIntegerField(default=0, help_text='uv', verbose_name='uv')),
                ('read_times', models.PositiveIntegerField(default=0, help_text='阅读次数', verbose_name='阅读次数')),
                ('is_top', models.BooleanField(default=False, help_text='是否置顶', verbose_name='是否置顶')),
                ('read_time', models.PositiveIntegerField(default=0, help_text='预计阅读时长', verbose_name='预计阅读时长')),
                ('quality_score', models.PositiveIntegerField(default=10, help_text='质量分数', verbose_name='质量分数')),
                ('recommendation_score', models.PositiveIntegerField(default=0, help_text='推荐分数', verbose_name='推荐分数')),
                ('is_draft', models.BooleanField(default=True, help_text='是否是草稿', verbose_name='是否是草稿')),
                ('is_original', models.BooleanField(default=True, help_text='是否原创', verbose_name='是否原创')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'db_table': '博客',
                'ordering': ['-is_top', '-update_time'],
            },
        ),
        migrations.CreateModel(
            name='BlogTagRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '博客_标签关系表',
                'verbose_name_plural': '博客_标签关系表',
                'db_table': '博客_标签关系表',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('title', models.CharField(blank=True, help_text='标题', max_length=8, unique=True, verbose_name='标题')),
                ('avatar', models.URLField(default='image/default_blog_avatar.jpg', help_text='封面', verbose_name='封面')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': '分类',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('is_canceled', models.BooleanField(default=False, help_text='收藏是否已取消', verbose_name='收藏是否已取消')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
                'db_table': '收藏',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('content', models.CharField(help_text='评论内容', max_length=500, verbose_name='评论内容')),
                ('ip', models.CharField(help_text='ip地址', max_length=32, verbose_name='ip地址')),
                ('client', models.CharField(help_text='设备', max_length=20, verbose_name='设备')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': '评论',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('is_canceled', models.BooleanField(default=False, help_text='点赞是否已取消', verbose_name='点赞是否已取消')),
            ],
            options={
                'verbose_name': '点赞',
                'verbose_name_plural': '点赞',
                'db_table': '点赞',
            },
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
            ],
            options={
                'verbose_name': '相关推荐',
                'verbose_name_plural': '相关推荐',
                'db_table': '相关推荐',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('keyword', models.CharField(help_text='关键字', max_length=100, verbose_name='关键字')),
                ('result', models.CharField(help_text='搜索结果', max_length=100, verbose_name='搜索结果')),
            ],
            options={
                'verbose_name': '搜索记录',
                'verbose_name_plural': '搜索记录',
                'db_table': '搜索记录',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('title', models.CharField(blank=True, help_text='标题', max_length=30, verbose_name='标题')),
                ('avatar', models.URLField(default='image/default_blog_avatar.jpg', help_text='封面', verbose_name='封面')),
            ],
            options={
                'ordering': ['-update_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('title', models.CharField(blank=True, help_text='标题', max_length=5, unique=True, verbose_name='标题')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': '标签',
            },
        ),
    ]
