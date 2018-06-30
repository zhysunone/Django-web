# _*_ encoding=utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models

from organization.models import  CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    """课程信息"""
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50,verbose_name=u"课程名")
    desc = models.CharField(max_length=200,verbose_name=u"课程描述")
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/", filePath="courses/ueditor/", default="")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True)
    degree = models.CharField(verbose_name=u"难度",choices=(("cj",u"初级"),("zj",u"中级"),("gj",u"高级")),max_length=2)
    learn_time = models.IntegerField(default=0,verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面图片",max_length=100)
    # 点击数和课程学习数不一样.
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    category = models.CharField(default=u"后端开发", max_length=20,verbose_name=u"课程类别")
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()
    # 在xadmin里面自定义这个字段名称
    get_zj_nums.short_description = "章节数"

    def go_to(self):
        # 跳转
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</>")
    go_to.short_description = "跳转"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        #获取课程所有章节
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    """
    继承课程信息,在xadmin里面注册不同的数据
    """
    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
        proxy = True

class Lesson(models.Model):
    """章节信息"""
    course = models.ForeignKey(Course,verbose_name=u"课程")
    # 章节里面有一个外键指向课程信息
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        #获取章节视频
        return self.video_set.all()


class Video(models.Model):
    """视频信息"""
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    # 外键指向章节
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    """课程资源"""
    course = models.ForeignKey(Course, verbose_name=u"课程")
    # 指向课程外键
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
