# _*_ encoding=utf-8 _*_
#为了遵循python的PEP8的规范
#第一块python自带的
from __future__ import unicode_literals
from datetime import datetime

#第二块第三方(django)的
from django.db import models
# 继承系统中自带的user字段
from django.contrib.auth.models import AbstractUser

#第三块自己写的类


# Create your models here.


class UserProfile(AbstractUser):
    """
    添加自己的字段 用UserProfile覆盖系统user
    """
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称",default=u"")
    birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=10,choices=(("male",u"男"),("female",u"女")),default=u"female")
    address = models.CharField(max_length=100,default=u"")
    # null=True blank= True 该字段可以为空 null,blank 默认为False
    mobile = models.CharField(max_length=11,null=True,blank=True)
    # upload_to指定上传的路径   default默认
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=500)

    class Meta:
        verbose_name = "用户信息"
        # 指定改对象一个更好的名字(复数)
        verbose_name_plural = verbose_name

    #重载unicode方法
    def __unicode__(self):
        return self.username

    def unread_nums(self):
        # 获取用户未读消息的数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class EmailVerifyRecord(models.Model):
    """
    邮箱验证码
    """
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型",choices=(("register",u"注册"),("forget",u"找回密码"),("update_email",u"修改邮箱")),max_length=30)
    #now加括号表示是model编译的时间,不加括号表示的是实例化这个对象的时间
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    """首页轮播图"""
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图",max_length=100)
    #点击轮播图片跳转
    url = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    # now 加括号表示当前编译时间,不加括号表示类运行的时间(实例化这个对象的时间).
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")


    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

