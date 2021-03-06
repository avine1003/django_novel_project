from DjangoUeditor.models import UEditorField
from django.db import models
from django.utils import timezone


# Create your models here.

# 小说标签
class Tag(models.Model):
    t_name = models.CharField(max_length=100, verbose_name='标签名')
    t_info = models.CharField(max_length=200, verbose_name='标签描述')
    t_addtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='添加时间')

    def __str__(self):
        return self.t_name

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = '标签'


# 文章表
class Art(models.Model):
    a_title = models.CharField(max_length=100, verbose_name='标题')
    a_info = models.CharField(max_length=300, verbose_name='简介')
    # a_content = models.TextField(verbose_name='内容')
    a_content = UEditorField(verbose_name='内容', width=1000, height=600,
                             imagePath="arts_ups/ueditor/", filePath="arts_ups/ueditor/",
                             blank=True, toolbars="full", default='')
    a_img = models.ImageField(verbose_name='图片', upload_to='arts_ups/%Y/%m/')
    a_addtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='添加时间')
    a_tag = models.ForeignKey(Tag, verbose_name='标签')

    def __str__(self):
        return self.a_title

    class Meta:
        db_table = 'art'
        verbose_name = '小说'
        verbose_name_plural = '小说'
        ordering = ['-a_addtime']
