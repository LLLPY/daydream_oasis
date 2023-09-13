# Generated by Django 4.1.5 on 2023-09-13 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(help_text='创建者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='section',
            name='creator',
            field=models.ForeignKey(help_text='创建者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='search',
            name='user',
            field=models.ForeignKey(help_text='搜索者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='搜索者'),
        ),
        migrations.AddField(
            model_name='recommend',
            name='blog_list',
            field=models.ManyToManyField(help_text='博客列表', to='blog.blog', verbose_name='博客列表'),
        ),
        migrations.AddField(
            model_name='recommend',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='like',
            name='blog',
            field=models.ForeignKey(help_text='被点赞的博客', on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='被点赞的博客'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(help_text='点赞人', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='点赞人'),
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(help_text='被评论的博客', on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='被评论的博客'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(help_text='父评论', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment', verbose_name='父评论'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(help_text='评论人', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论人'),
        ),
        migrations.AddField(
            model_name='collection',
            name='blog',
            field=models.ForeignKey(help_text='被收藏的博客', on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='被收藏的博客'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(help_text='收藏人', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏人'),
        ),
        migrations.AddField(
            model_name='category',
            name='creator',
            field=models.ForeignKey(help_text='创建者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='blogtagrelease',
            name='blog',
            field=models.ForeignKey(help_text='博客', on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='博客'),
        ),
        migrations.AddField(
            model_name='blogtagrelease',
            name='tag',
            field=models.ForeignKey(help_text='标签', on_delete=django.db.models.deletion.CASCADE, to='blog.tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(help_text='作者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(help_text='分类', on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='blog',
            name='section',
            field=models.ForeignKey(help_text='专栏', on_delete=django.db.models.deletion.CASCADE, to='blog.section', verbose_name='专栏'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(help_text='标签', related_name='blogs', to='blog.tag', verbose_name='标签'),
        ),
    ]
