# Generated by Django 4.1.5 on 2023-09-13 19:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('path', models.TextField(default='/', help_text='请求路径', max_length=1000, verbose_name='请求路径')),
                ('path_type', models.PositiveIntegerField(choices=[(0, '页面'), (1, '媒体文件'), (2, 'API接口'), (3, '其他')], default=0, help_text='请求路径类型', verbose_name='请求路径类型')),
                ('method', models.CharField(default='GET', help_text='请求方式', max_length=100, verbose_name='请求方式')),
                ('user_agent', models.CharField(help_text='请求头', max_length=500, verbose_name='请求头')),
                ('http_refer', models.URLField(help_text='跳转的网页', verbose_name='跳转的网页')),
                ('os', models.CharField(default='', help_text='操作系统', max_length=100, verbose_name='操作系统')),
                ('country', models.CharField(default='', help_text='国家', max_length=50, verbose_name='国家')),
                ('province', models.CharField(default='', help_text='省份', max_length=50, verbose_name='省份')),
                ('city', models.CharField(default='', help_text='城市', max_length=50, verbose_name='城市')),
                ('computer_name', models.CharField(default='', help_text='计算机名', max_length=50, verbose_name='计算机名')),
                ('username', models.CharField(default='', help_text='用户名', max_length=50, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '请求日志',
                'verbose_name_plural': '请求日志',
                'db_table': '请求日志',
            },
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('reason', models.CharField(help_text='错误原因', max_length=500, verbose_name='错误原因')),
                ('time', models.DateTimeField(default=datetime.datetime.now, help_text='时间', verbose_name='时间')),
                ('request_log', models.ForeignKey(help_text='请求对象', on_delete=django.db.models.deletion.CASCADE, to='log.requestrecord', verbose_name='请求对象')),
            ],
            options={
                'verbose_name': '错误日志',
                'verbose_name_plural': '错误日志',
                'db_table': '错误日志',
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('desc', models.CharField(help_text='简介', max_length=300, verbose_name='简介')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('uuid', models.CharField(help_text='uuid,对于没有登录的用户的唯一标识', max_length=200, verbose_name='uuid')),
                ('action', models.PositiveIntegerField(choices=[(0, '点赞'), (1, '取消点赞'), (2, '收藏'), (3, '取消收藏'), (4, '评论'), (5, '删除评论'), (6, '点击'), (7, '阅读'), (8, '打赏')], help_text='行为', verbose_name='行为')),
                ('cost_time', models.FloatField(default=0, help_text='耗时', verbose_name='耗时')),
                ('score', models.IntegerField(default=0, help_text='分值', verbose_name='分值')),
                ('blog', models.ForeignKey(help_text='博客', on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='博客')),
            ],
            options={
                'verbose_name': '操作日志',
                'verbose_name_plural': '操作日志',
                'db_table': '操作日志',
            },
        ),
    ]