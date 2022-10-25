from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
所有模型都是django.db.models.Model类的⼦类。每个类将被转换为数据库表。
每个字段由 django.db.models.Field⼦类（内置在Django core）的实例表示，它们并将被转换为数据库的列。
"""


class Board(models.Model):  #这是一个模型，在admin中添加模型意思就是添加的这个
    """
    name 和 description。 name字段必须是唯⼀的，为了避免有重复的名称。
    description ⽤于说明这个版块是做什么⽤的。

    参数unique=True  ，顾名思义(unique意为独一无二)，它将强制数据库级别字段的唯⼀性。
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()
    # ⽤这个Board实例来过滤这个 QuerySet
    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

    def __str__(self):
        return self.name

"""
字段 CharField，DateTimeField等等，都是 django.db.models.Field 的⼦类。
包含在Django的核⼼⾥⾯-随时可以使⽤。
还有： 
CharField，TextField，DateTimeField、IntegerField，BooleanField， DecimalField、ForeignKey
"""



class Topic(models.Model):
    """
    subject 表示主题内容，last_update ⽤来定义话题的排序，
    starter ⽤来识别谁发起的话题，board ⽤于指定它属于哪个版块。
    """
    subject = models.CharField(max_length=255) #参数是数据库列的一个单元格的字符是多大
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')

class Post(models.Model):
    """
     message 字段，⽤于存储回复的内容，
     created_at 在排序时候⽤（最先发表的帖⼦排最前⾯），
    updated_at 告诉⽤户是否更新了内容，
    同时，还需要有对应的 User 模型的引⽤，Post 由谁创建的和谁更新的。

    """
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    #参数意思是django创建Post对象时为当前日期和时间
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    """
    模型之间的关系使⽤ ForeignKey  字段。它将在模型之间创建⼀个连接，并
    在数据库级别创建适当的关系（译注：外键关联）。该 ForeignKey  字段需
    要⼀个位置参数 related_name  ，⽤于引⽤它关联的模型。
    （译注：例如created_by 是外键字段，关联的User模型，表明这个帖⼦是谁创建的，
    related_name=posts 表示在 User 那边可以使⽤ user.posts 来查看这个⽤户
    创建了哪些帖⼦）
    例如，在 Topic  模型中， board  字段是 Board  模型的 ForeignKey  。它
        告诉Django，⼀个 Topic  实例只涉及⼀个Board实例。 related_name  参数
        将⽤于创建反向关系， Board  实例通过属性 topics  访问属于这个版块下
        的 Topic  列表。
    """