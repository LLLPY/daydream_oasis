import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import BaseModel
from django.db import models
from lxml import etree
from user.models import User
from utils.cache import my_cache
from utils.collaborative_filltering import cf_user
import re


# 博客分类
class Category(BaseModel):
    # 创建者
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者', help_text='创建者')

    # 标题
    title = models.CharField(max_length=8, blank=True, unique=True, verbose_name='标题', help_text='标题')

    # avatar
    avatar = models.URLField(default='image/default_blog_avatar.jpg', verbose_name='封面', help_text='封面')

    # 父类
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    # 深度
    depth = models.SmallIntegerField(default=1, help_text='深度', verbose_name='深度')

    class Meta:
        db_table = '分类'  # 修改表名
        verbose_name_plural = verbose_name = db_table

    @classmethod
    def get_by_name(cls, name):
        return cls.objects.filter(title=name).first()


# 标签
class Tag(BaseModel):
    # 创建者
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者', help_text='创建者')

    # title
    title = models.CharField(max_length=5, blank=True, unique=True, verbose_name='标题', help_text='标题')

    class Meta:
        db_table = '标签'
        verbose_name_plural = verbose_name = db_table


# 专栏
class Section(BaseModel):
    '''专栏'''

    # title
    title = models.CharField(max_length=30, blank=True, verbose_name='标题', help_text='标题')

    # 创建者
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者', help_text='创建者')

    # 封面
    avatar = models.URLField(default='image/default_blog_avatar.jpg', verbose_name='封面', help_text='封面')


# 博客
class Blog(BaseModel):
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', help_text='作者')

    # 标题
    title = models.CharField(max_length=30, blank=True, verbose_name='标题', help_text='标题')

    # 封面
    avatar = models.URLField(default='image/default_blog_avatar.jpg', verbose_name='封面', help_text='封面')

    # 专栏
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, verbose_name='专栏', help_text='专栏')

    # 分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', help_text='分类')

    # 标签
    tag_list = models.ManyToManyField(Tag, verbose_name='标签', help_text='标签', related_name='blogs')

    # 摘要
    abstract = models.TextField(max_length=150, null=False, blank=False, verbose_name='摘要', help_text='摘要')

    # 文章正文
    content = RichTextUploadingField(null=False, blank=False, verbose_name='文章内容', help_text='文章内容')

    # daily page view
    dpv = models.PositiveIntegerField(default=0, verbose_name='dpv', help_text='dpv')

    # daily  unique visitor
    duv = models.PositiveIntegerField(default=0, verbose_name='duv', help_text='duv')

    # page view(浏览总量)
    pv = models.PositiveIntegerField(default=0, verbose_name='pv', help_text='pv')

    # unique visitor(总访客量)
    uv = models.PositiveIntegerField(default=0, verbose_name='uv', help_text='uv')

    # 阅读次数
    read_times = models.PositiveIntegerField(default=0, verbose_name='阅读次数', help_text='阅读次数')

    # 是否置顶
    is_top = models.BooleanField(default=False, verbose_name='是否置顶', help_text='是否置顶')

    # 预计阅读时长
    read_time = models.PositiveIntegerField(default=0, verbose_name='预计阅读时长', help_text='预计阅读时长')

    # 质量分数
    quality_score = models.PositiveIntegerField(default=10, verbose_name='质量分数', help_text='质量分数')

    # 推荐分数 (临时变量，用于给用户推荐使用)
    recommendation_score = models.PositiveIntegerField(default=0, verbose_name='推荐分数', help_text='推荐分数')

    # 草稿
    is_draft = models.BooleanField(default=True, verbose_name='是否是草稿', help_text='是否是草稿')

    # 是否原创
    is_original = models.BooleanField(default=True, verbose_name='是否原创', help_text='是否原创')

    class Meta:
        db_table = '博客'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-is_top', '-update_time']

    @classmethod
    def get_count_by_category_id(cls, category_id: str) -> int:
        return cls.objects.filter(category_id=category_id).count()

    # 更新阅读时长
    def update_read_time(self) -> None:
        '''
        阅读时长计算公式:cost_time=总字数÷平均阅读速度+图片数*5
        '''
        text_list = re.findall(r'[\u4e00-\u9fa5|a-z|A-Z]+', self.content)
        text_len = len(''.join(text_list))
        img_count = len(etree.HTML(self.content).xpath('//img'))
        avg_speed = 400  # 除以3的原因：内容中除了中文以外可能还有英文
        read_time = 60 * (text_len / avg_speed) / 3 + img_count * 5
        self.read_time = read_time

    # 转换阅读时间的显示方式
    def transform_read_time(self):
        minute = int(self.read_time) // 60
        seconds = int(self.read_time) % 60
        self.read_time = f'{minute}分{seconds}秒'
        return self.read_time

    @classmethod
    def create_or_update(cls, _id: str, title: str, avatar: str, category: Category, tag_list: [], content: str,
                         author: User) -> 'Blog':
        tmp_blog = cls.get_by_id(_id)
        if tmp_blog:
            tmp_blog.update_time = datetime.datetime.now()
        else:
            tmp_blog = cls()
        tmp_blog.title = title
        tmp_blog.author = author
        if avatar:
            tmp_blog.avatar = avatar
        tmp_blog.category = category
        tmp_blog.content = content
        # 摘要为内容的前150字
        tmp_blog.abstract = ''.join(
            etree.HTML(content).xpath('//text()'))[:150]
        # 更新阅读时长
        tmp_blog.update_read_time()
        for tag in tag_list:
            tag = Tag.get_or_create(tag, creator=author)
            tmp_blog.tags.add(tag)
        tmp_blog.save()

        return tmp_blog

    @classmethod
    def recommend(cls, user, action_data, blog_list=[]):

        # 添加缓存，提高性能
        blog_list = cls.objects.filter(has_deleted=False).only('id', 'title', 'avatar', 'abstract', 'pv',
                                                               'create_time', 'is_top', 'author', 'category')

        # 根据用户操作的历史数据来生成推荐列表

        # 用户操作的历史数据
        recommend_dict = cf_user(user, action_data)

        # 用户自己的操作历史
        user_action_history = action_data.get(user, {})
        for k in user_action_history:
            recommend_dict[k] = user_action_history[k]

        # 衰减函数 推荐度随时间衰减
        def lose_func(t, base=100, alpha=0.8):
            return base * 1 / pow((1 + t), alpha)

        # 刷新每篇文章的推荐分数
        recommend_blog_list = []
        for blog in blog_list:
            # 文章的关于时间的推荐度
            days = (datetime.datetime.now() - blog.create_time).days
            recommendation_score = recommend_dict.get(blog.id, 0) + lose_func(days, 100 + blog.dpv)

            blog.recommendation_score = recommendation_score
            recommend_blog_list.append(blog)
        # 根据推荐分进行排序
        recommend_blog_list.sort(key=lambda a: -a.recommendation_score)

        return recommend_blog_list


class BlogTagRelease(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='博客', help_text='博客')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签', help_text='标签')

    class Meta:
        db_table = '博客_标签关系表'
        verbose_name = verbose_name_plural = db_table


# 用户评论表
class Comment(BaseModel):
    # 评论人
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论人', help_text='评论人')

    # 评论的博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='被评论的博客', help_text='被评论的博客')

    # 评论内容
    content = models.CharField(max_length=500, verbose_name='评论内容', help_text='评论内容')

    # 父评论
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, verbose_name='父评论', help_text='父评论')

    # 设备 手机 电脑
    client = models.CharField(max_length=20, verbose_name='设备', help_text='设备')

    class Meta:
        db_table = '评论'
        verbose_name = verbose_name_plural = db_table

    # 根据博客id获取该博客下的评论量
    @classmethod
    def get_count_by_blog(cls, blog: Blog) -> int:
        return cls.objects.filter(blog=blog).count()


class LikeMixin:

    @classmethod
    def get_count(cls, blog: Blog):
        '''获取指定博客的点赞数量'''
        return cls.objects.filter(blog=blog).count()

    @classmethod
    def status(cls, blog: Blog, user: User):
        '''判断当前用户是否点赞'''
        if not user.is_authenticated:
            return (None, False)
        self = cls.objects.filter(blog=blog, user=user).first()
        return (self, True) if self else (None, False)

    @classmethod
    def create(cls, blog: Blog, user: User):
        self = cls()
        self.blog = blog
        self.user = user
        self.save()


# 点赞记录表
class Like(BaseModel, LikeMixin):
    # 点赞人
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='点赞人', help_text='点赞人')

    # 被点赞的博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='被点赞的博客', help_text='被点赞的博客')

    class Meta:
        db_table = '点赞'
        verbose_name = verbose_name_plural = db_table


# 收藏记录表
class Collection(BaseModel, LikeMixin):
    # 收藏人
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='收藏人', help_text='收藏人')

    # 被收藏的博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='被收藏的博客', help_text='被收藏的博客')

    class Meta:
        db_table = '收藏'
        verbose_name = verbose_name_plural = db_table


# 分享记录表
class Share(BaseModel, LikeMixin):
    # 分享人
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='分享人', help_text='分享人')

    # 被分享的博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='被分享的博客', help_text='被分享的博客')

    class Meta:
        db_table = '分享'
        verbose_name = verbose_name_plural = db_table


# 搜索记录表
class Search(BaseModel):
    # 关键字
    keyword = models.CharField(max_length=100, verbose_name='关键字', help_text='关键字')

    # 搜索者
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='搜索者', help_text='搜索者')

    # 结果
    result = models.CharField(max_length=100, verbose_name='搜索结果', help_text='搜索结果')

    class Meta:
        db_table = '搜索记录'
        verbose_name = verbose_name_plural = db_table

    @classmethod
    def create(cls, keyword: str, user: User) -> 'Search':
        user = user if user.is_authenticated else User.get_by_id('1')
        obj = cls(keyword=keyword, user=user)
        obj.save()
        return obj


# 相关推荐
class Recommend(BaseModel):
    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户')

    # 推荐的博客列表
    blog_list = models.ManyToManyField(Blog, verbose_name='博客列表', help_text='博客列表')

    class Meta:
        db_table = '相关推荐'
        verbose_name = verbose_name_plural = db_table

    @classmethod
    def get_by_user(cls, user: User):
        if not user.is_authenticated:
            return []
        tmp_recommend = cls.objects.filter(user=user).first()
        if not tmp_recommend:
            return []
        else:
            return tmp_recommend.blog_list.all()
