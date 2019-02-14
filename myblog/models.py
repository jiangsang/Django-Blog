from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model):
    title = models.CharField(u"博客标题", max_length=100)  # 博客标题
    category = models.CharField(u"博客标签", max_length=50, blank=True)  # 博客标签
    desc = models.CharField(u"博客描述", max_length=50, blank=True,null=True)  # 博客描述
    headpicture = models.ImageField("封面图片",default=u'',null=True, blank=True, upload_to='uploads/blog/images/')
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)  # 博客发布日期
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    content = UEditorField(u"文章正文", height=300, width=790, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"
# 留言模型
class Leacot(models.Model):
    blog = models.ForeignKey(Article, on_delete=models.CASCADE, default=1)
    content = models.CharField(max_length=140)
    time = models.DateTimeField(auto_now_add=True)
# 照片模型
class Photo(models.Model):
    photo = models.ImageField(default=u'', blank=True, upload_to='uploads/photos/images/')
    name = models.CharField("照片标题",max_length=50,null=True)
    place = models.CharField("拍摄地址",max_length=60)
    time = models.DateTimeField("拍摄时间",null=True)
    update_time = models.DateTimeField(u'上传时间', auto_now=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:  # 按时间下降排序
        ordering = ['-update_time']
        verbose_name = "相册"
        verbose_name_plural = "相册 "