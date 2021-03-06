# _*_ coding:utf-8  _*_

__author__ = 'bobby'
__date__ = '2017/10/12 14:36'
from django import forms
from captcha.fields import CaptchaField


from.models import UserProfile

# 存储form定义的文件

class LoginForm(forms.Form):
    # ruquired=True 表示这个字段为必填字段
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 抛出指定的错误
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误!"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误!"})

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'birday', 'gender', 'address', 'mobile']

