# _*_ coding:utf-8  _*_
"""
设置的方法:
    在setting中搜索templates 然后找到find and code...  然后再python script中添加utf-8编码
    date设置为$DATE $TIME 就可以自动获取当前的时间
"""
__author__ = 'bobby'
__date__ = '2017/10/10 11:25'


import xadmin

from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord,Banner,UserProfile

from xadmin.layout import Fieldset, Main, Side, Row, FormHelper
from xadmin.sites import site
from django.utils.translation import ugettext as _

# 这个py文件的功能是把model的信息注册到后台管理系统中
class UserProfileAdmin(UserAdmin):
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


class BaseSetting(object):
    """配置xadmin的主题功能"""
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """配置xadmin的页头和页尾"""
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    # 收起xadmin里面每个项目下的小章节
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 列表中显示哪些字段, 顺序和这个顺序是一样的
    # list_display search_fields list_filter 固定写法不能修改(时间不好搜索,所以直接去掉了)
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    # list_filter 过滤器字段,通过过滤快速搜索
    list_filter = ['code','email','send_type','send_time']
    # xadmin图标的修改
    # model_icon = 'fa fa-address-book-o'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']



# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
