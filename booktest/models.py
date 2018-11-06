from django.db import models


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    # btitle = models.CharField(max_length=20)#图书名称
    btitle = models.CharField(max_length=20, db_column='title')  # 通过db_column指定btitle对应表格中字段的名字为title
    bpub_date = models.DateField()
    # 发布日期
    bread = models.IntegerField(default=0)
    # 阅读量
    bcomment = models.IntegerField(default=0)
    # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    # 定义英雄模型类HeroInfo


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    # hcomment = models.CharField(max_length=200)#英雄描述信息
    hcomment = models.CharField(max_length=200, null=True,
                                blank=False)  # hcomment对应的数据库中的字段可以为空，但通过后台管理页面添加英雄信息时hcomment对应的输入框不能为空
    hbook = models.ForeignKey('BookInfo')  # 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中


# 定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)  # 名称
    aParent = models.ForeignKey('self', null=True, blank=True)  # 关系
