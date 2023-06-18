import datetime
from typing import Dict, List
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import BaseModel
from common.my_cache import my_cache
from django.db import models
from django.db.models import Q
from lxml import etree
from user.models import User
from utils.collaborative_filltering import cf_user
from django.core.cache import cache


# 博客分类
class Category(models.Model, BaseModel):
    # 标题
    title = models.CharField(max_length=8, blank=True, unique=True,
                             db_column='标题', verbose_name='标题', help_text='标题')

    # 创建时间
    time = models.DateTimeField(
        default=datetime.datetime.now, db_column='创建时间', verbose_name='创建时间', help_text='创建时间')

    # 创建者
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='创建者', verbose_name='创建者', help_text='创建者')

    fields = ['title', 'time', 'creator']

    class Meta:
        db_table = '分类'  # 修改表名
        verbose_name_plural = verbose_name = db_table
        # ordering = ['-used_count']

    def __str__(self) -> str:
        return self.title

    @classmethod
    @my_cache(timeout=60 * 60)
    def get_all(cls) -> Dict:
        return {category.title: {'id': category.id, 'times': category.blog_set.count()} for category in
                cls.objects.all()}

    @classmethod
    def get_by_title(cls, title: str) -> 'Category':
        category_obj = Category.objects.filter(title=title).first()
        if not category_obj:  # 如果数据库中没有该类,则新建该类
            category_obj = Category()
            category_obj.title = title
            category_obj.save()
        return category_obj

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list, extra_map)


# 标签
class Tag(models.Model, BaseModel):
    # title
    title = models.CharField(max_length=5, blank=True, unique=True,
                             db_column='标题', verbose_name='标题', help_text='标题')

    # 创建时间
    time = models.DateTimeField(
        default=datetime.datetime.now, db_column='创建时间', verbose_name='创建时间', help_text='创建时间')

    # 创建者
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='创建者', verbose_name='创建者', help_text='创建者')

    fields = ['title', 'time', 'creator']

    class Meta:
        db_table = '标签'
        verbose_name_plural = verbose_name = db_table

    def __str__(self) -> str:
        return self.title

    @classmethod
    @my_cache(timeout=60 * 60)
    def get_all(cls) -> Dict:
        return {tag.title: {'id': tag.id, 'times': tag.blogs.count()} for tag in cls.objects.all()}

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list, extra_map)


# 博客
class Blog(models.Model, BaseModel):
    # 作者
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='作者', verbose_name='作者', help_text='作者')

    # 标题
    title = models.CharField(max_length=30, blank=True,
                             db_column='标题', verbose_name='标题', help_text='标题')

    # 封面
    avatar = models.CharField(max_length=500, blank=True, default='image/default_blog_avatar.jpg',
                              db_column='封面',
                              verbose_name='封面',
                              help_text='封面')

    # 专栏 TODO 下一个版本开发
    # section=models.ForeignKey()

    # 分类
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='分类', verbose_name='分类', help_text='分类')

    # 标签
    tags = models.ManyToManyField(
        Tag, db_column='标签', verbose_name='标签', help_text='标签', related_name='blogs')

    # 摘要
    abstract = models.TextField(max_length=150, null=False, blank=False, db_column='摘要', verbose_name='摘要',
                                help_text='摘要')

    # 文章正文
    # content = models.TextField(db_column='文章正文', verbose_name='文章正文')
    content = RichTextUploadingField(
        null=False, blank=False, db_column='文章内容', verbose_name='文章内容', help_text='文章内容')

    # daily page view
    dpv = models.PositiveIntegerField(
        default=0, db_column='dpv', verbose_name='dpv', help_text='dpv')

    # daily  unique visitor
    duv = models.PositiveIntegerField(
        default=0, db_column='duv', verbose_name='duv', help_text='duv')

    # page view(浏览总量)
    pv = models.PositiveIntegerField(
        default=0, db_column='pv', verbose_name='pv', help_text='pv')

    # unique visitor(总访客量)
    uv = models.PositiveIntegerField(
        default=0, db_column='uv', verbose_name='uv', help_text='uv')

    # 获赞量
    # likes = models.PositiveIntegerField(default=0, db_column='获赞量', verbose_name='获赞量', help_text='获赞量')

    # 收藏量
    # collections = models.PositiveIntegerField(default=0, db_column='收藏量', verbose_name='收藏量', help_text='收藏量')

    # 创建时间
    create_time = models.DateTimeField(default=datetime.datetime.now, db_column='创建时间', verbose_name='创建时间',
                                       help_text='创建时间')

    # 文章最后修改的时间
    update_time = models.DateTimeField(default=datetime.datetime.now, db_column='最后修改时间', verbose_name='最后修改时间',
                                       help_text='最后修改时间')

    # 文章是否已删除
    is_deleted = models.BooleanField(
        default=False, db_column='文章是否已删除', verbose_name='文章是否已删除', help_text='文章是否已删除')

    # 是否置顶
    is_top = models.BooleanField(
        default=False, db_column='是否置顶', verbose_name='是否置顶', help_text='是否置顶')

    # 预计阅读时长
    read_time = models.PositiveIntegerField(
        default=0, db_column='预计阅读时长', verbose_name='预计阅读时长', help_text='预计阅读时长')

    # 质量分数
    quality_score = models.PositiveIntegerField(
        default=10, db_column='质量分数', verbose_name='质量分数', help_text='质量分数')

    # 推荐分数 (临时变量，用于给用户推荐使用)
    recommendation_score = models.PositiveIntegerField(default=0, db_column='推荐分数', verbose_name='推荐分数',
                                                       help_text='推荐分数')

    fields = ['id', 'title', 'author', 'avatar', 'category', 'tags', 'abstract', 'content', 'dpv', 'duv', 'pv', 'uv',
              'likes', 'collections', 'comments', 'create_time', 'update_time', 'read_time',
              'quality_score', 'recommendation_score']

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = '博客'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-is_top', '-create_time']

    @classmethod
    def get_all(cls):
        return cls.objects.filter(is_deleted=False).all()

    @classmethod
    def get_by_id(cls, _id: str) -> 'Blog':
        return cls.objects.filter(id=_id).first()

    @classmethod
    def get_count_by_category_id(cls, category_id: str) -> int:
        return cls.objects.filter(category_id=category_id).count()

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        con = super().to_dict(fields, exclude_list, extra_map)
        diff_set = set(fields) - set(exclude_list)
        if 'likes' in diff_set:
            con['likes'] = Like.get_count_by_blog(self)
        if 'collections' in diff_set:
            con['collections'] = Like.get_count_by_blog(self)
        if 'comments' in diff_set:
            con['comments'] = Comment.get_count_by_blog(self)
        return con

    # 搜索
    @classmethod
    def search(cls, keyword_list: List[str]):
        # 使用原生sql语句查询时，%需要成对存在，否则会报错
        sql = f'''SELECT id, 标题, 封面, 摘要, pv, 创建时间, 是否置顶, 作者, 分类 FROM 博客 where 文章是否已删除="否" and 标题 like "%%{keyword_list[0]}%%" or 文章内容 like "%%{keyword_list[0]}%%"'''
        for keyword in keyword_list[1:]:
            sql += f' or 标题 like "%%{keyword}%%" or 文章内容 like "%%{keyword}%%"'
        # 按照浏览量排序
        sql += ' order by pv'
        return cls.objects.raw(sql)

    # 更新阅读时长
    def update_read_time(self) -> None:
        '''
        阅读时长计算公式:cost_time=总字数÷平均阅读速度+图片数*5
        '''
        content = etree.HTML(self.content).xpath('//text()')
        content = ''.join(
            [con.replace('\xa0', '').replace('\n', '').replace('\r', '').replace(' ', '') for con in content])
        text_len = len(str(content))
        img_count = len(etree.HTML(self.content).xpath('//img'))
        avg_speed = 400  # 除以3的原因：内容中除了中文以外可能还有英文
        read_time = 60 * (text_len / avg_speed) / 3 + img_count * 5
        self.read_time = read_time

    # 转换阅读时间的显示方式
    def transform_read_time(self) -> None:
        minute = int(self.read_time) // 60
        seconds = int(self.read_time) % 60
        self.read_time = f'{minute}分{seconds}秒'

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
    @my_cache(60 * 60)
    def recommend(cls, user, action_data, blog_list=[]):

        # 添加缓存，提高性能
        if not blog_list:
            blog_list = cache.get('blog_list')
            if not blog_list:
                blog_list = cls.objects.filter(is_deleted=False).only('id', 'title', 'avatar', 'abstract', 'pv',
                                                                      'create_time', 'is_top', 'author', 'category')
                cache.set('blog_list', blog_list, 3600)

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


class Blog_Tag_Release(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, db_column='博客', verbose_name='博客',
                             help_text='博客')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, db_column='标签', verbose_name='标签', help_text='标签')

    class Meta:
        db_table = '博客_标签关系表'
        verbose_name = verbose_name_plural = db_table


# 用户评论表
class Comment(models.Model, BaseModel):
    # 评论人
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='评论人', verbose_name='评论人',
                             help_text='评论人')

    # 评论的博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, db_column='被评论的博客', verbose_name='被评论的博客',
                             help_text='被评论的博客')

    # 评论内容
    content = models.CharField(
        max_length=500, db_column='评论内容', verbose_name='评论内容', help_text='评论内容')

    # 评论时间
    time = models.DateTimeField(
        default=datetime.datetime.now, db_column='评论时间', verbose_name='评论时间', help_text='评论时间')

    # 是否显示 如果用户删除评论后 该评论就不被显示
    is_deleted = models.BooleanField(
        default=False, db_column='是否已删除', verbose_name='是否已删除', help_text='是否已删除')

    fields = ['id', 'user', 'blog', 'content', 'time']

    class Meta:
        db_table = '评论'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-time']

    # 根据博客id获取该博客下的评论量
    @classmethod
    def get_count_by_blog(cls, blog: Blog) -> int:
        return cls.objects.filter(Q(blog=blog) & Q(is_deleted=False)).count()

    @classmethod
    def get_by_id(cls, _id: int) -> 'Comment':
        return cls.objects.filter(id=_id).first()

    @classmethod
    @my_cache(60)
    def get_all_by_blog(cls, blog_id: str) -> List[Dict]:
        comment_list = Comment.objects.filter(
            Q(blog_id=blog_id) & Q(is_deleted=False))
        con_list = []
        for comment in comment_list:
            extra_map = {
                'user': {'fields': ['id', 'username', 'avatar']},
                'blog': {'fields': ['id']},
            }
            con = comment.to_dict(extra_map=extra_map)
            con_list.append(con)
        return con_list

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list, extra_map)


# 收藏记录表
class Collection(models.Model, BaseModel):
    # 收藏人
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             db_column='收藏人', verbose_name='收藏人', help_text='收藏人')

    # 被收藏的博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, db_column='被收藏的博客', verbose_name='被收藏的博客',
                             help_text='被收藏的博客')

    # 是否取消收藏
    is_canceled = models.BooleanField(
        default=False, db_column='收藏是否已取消', verbose_name='收藏是否已取消', help_text='收藏是否已取消')

    # 收藏时的日期
    time = models.DateTimeField(
        default=datetime.datetime.now, db_column='收藏日期', verbose_name='收藏日期', help_text='收藏日期')

    fields = ['id', 'user', 'blog', 'is_canceled', 'time']

    class Meta:
        db_table = '收藏'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-time']

    # 判断某一篇文章是否被某一个用户收藏了
    @classmethod
    def is_collected(cls, user: 'User', blog: 'Blog') -> [int, int]:

        if not user.is_authenticated:
            return 0, 0

        tmp_collection = cls.objects.filter(
            Q(user=user) & Q(blog=blog)).first()
        if tmp_collection:
            if tmp_collection.is_canceled:
                return tmp_collection.id, 0
            else:
                return tmp_collection.id, 1
        else:
            return 0, 0

    @classmethod
    def get_by_id(cls, _id: str) -> 'Collection':
        return cls.objects.filter(id=_id).first()

    @classmethod
    def get_count_by_blog(cls, blog: Blog) -> int:
        return cls.objects.filter(Q(blog=blog) & Q(is_canceled=False)).count()

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list, extra_map)


# 点赞记录表
class Like(models.Model, BaseModel):
    # 点赞人
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             db_column='点赞人', verbose_name='点赞人', help_text='点赞人')

    # 被点赞的博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, db_column='被点赞的博客', verbose_name='被点赞的博客',
                             help_text='被点赞的博客')

    # 是否取消点赞
    is_canceled = models.BooleanField(
        default=False, db_column='点赞是否已取消', verbose_name='点赞是否已取消', help_text='点赞是否已取消')

    # 点赞时间
    time = models.DateTimeField(
        default=datetime.datetime.now, db_column='点赞时间', verbose_name='点赞时间', help_text='点赞时间')

    fields = ['id', 'user', 'blog', 'is_canceled', 'time']

    class Meta:
        db_table = '点赞'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-time']

    # 判断某一篇文章是否被某一个用户点赞了
    @classmethod
    def is_liked(cls, user: 'User', blog: 'Blog') -> [int, int]:
        if not user.is_authenticated:
            return 0, 0
        tmp_like = cls.objects.filter(Q(user=user) & Q(blog=blog)).first()
        if tmp_like:
            if tmp_like.is_canceled:
                return tmp_like.id, 0
            else:
                return tmp_like.id, 1
        else:
            return 0, 0
        # return tmp_like.id, True if tmp_like and not tmp_like.is_canceled else 0, False

    @classmethod
    def get_by_id(cls, _id: str) -> 'Like':
        return cls.objects.filter(id=_id).first()

    @classmethod
    def get_count_by_blog(cls, blog: Blog) -> int:
        return cls.objects.filter(Q(blog=blog) & Q(is_canceled=False)).count()

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list)


# 搜索记录表
class Search(models.Model, BaseModel):
    # 关键字
    keyword = models.CharField(
        max_length=100, db_column='关键字', verbose_name='关键字', help_text='关键字')

    # 搜索者
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             db_column='搜索者', verbose_name='搜索者', help_text='搜索者')

    # 搜索的日期
    time = models.DateTimeField(
        default=datetime.datetime.now, db_column='时间', verbose_name='时间', help_text='时间')

    fields = ['id', 'keyword', 'user', 'time']

    class Meta:
        db_table = '搜索记录'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-time']

    @classmethod
    def create(cls, keyword: str, user: User) -> 'Search':
        user = user if user.is_authenticated else User.get_by_id('1')
        obj = cls(keyword=keyword, user=user)
        obj.save()
        return obj

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list)


# 相关推荐
class Recommend(models.Model, BaseModel):
    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             db_column='用户', verbose_name='用户', help_text='用户')

    # 推荐的博客列表
    blog_list = models.ManyToManyField(
        Blog, db_column='博客列表', verbose_name='博客列表', help_text='博客列表')

    class Meta:
        db_table = '相关推荐'
        verbose_name = verbose_name_plural = db_table

    fields = ['id', 'user', 'blog_list']

    @classmethod
    def get_by_user(cls, user: User):
        if not user.is_authenticated:
            return []
        tmp_recommend = cls.objects.filter(user=user).first()
        if not tmp_recommend:
            return []
        else:
            return tmp_recommend.blog_list.all()

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list)
