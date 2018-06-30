# _*_ coding:utf-8  _*_

__author__ = 'bobby'
__date__ = '2017/10/23 9:16'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentsView



urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    url(r'^video/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_video"),

    #课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    url(r'^add_comments/(?P<course_id>\d+)/$', AddComentsView.as_view(), name="add_comments"),
]