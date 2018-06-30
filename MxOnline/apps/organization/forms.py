# _*_ coding:utf-8  _*_

__author__ = 'bobby'
__date__ = '2017/10/18 16:22'
import re
from  django import  forms

from  operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[34578]\d{9}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")