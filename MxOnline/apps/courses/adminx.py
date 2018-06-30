# _*_ coding:utf-8  _*_

__author__ = 'bobby'
__date__ = '2017/10/10 14:28'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg

class LessonInline(object):
    """
    在课程里面嵌套课程章节
    """
    model = Lesson
    extra = 0

class CourseResourceInline(object):
    """
    在课程里面嵌套课程资源
    """
    model = CourseResource
    extra = 0

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students','fav_nums','image','click_nums','add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name','desc','detail','degree','students','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_time','students','fav_nums','image','click_nums','add_time']
    # 点击数倒序排列
    ordering = ['-click_nums']
    # 设置为只读状态
    readonly_fields = ['click_nums']
    # 在xadmin页面直接修改字段内容
    list_editable = ['degree', 'desc']
    # 设置为隐藏状态
    exclude = ['fav_nums']
    # 在课程里面添加章节信息,课程资源信息
    inlines = [LessonInline, CourseResourceInline]

    # 在xadmin里面设置刷新时间
    # refresh_times = [3, 5]

    # 在xadmin中添加ueditor样式
    style_fields = {"detail": "ueditor"}

    # 在xadmin中导入excel
    # import_excel = True

    def queryset(self):
        """
         xadmin轮播图分类管理

        """
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


class BannerCourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name','desc','detail','degree','students','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_time','students','fav_nums','image','click_nums','add_time']
    # 点击数倒序排列
    ordering = ['-click_nums']
    # 设置为只读状态
    readonly_fields = ['click_nums']
    # 设置为隐藏状态
    exclude = ['fav_nums']
    # 在课程里面添加章节信息,课程资源信息
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_time', 'add_time']
    search_fields = ['course', 'name']
    #  course__name 外键的名字
    list_filter = ['course__name', 'name', 'learn_time', 'add_time']

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download','add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)