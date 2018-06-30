# _*_ coding:utf-8  _*_

__author__ = 'bobby'
__date__ = '2017/11/1 14:31'

#在xadmin中导入excel接口

# import xadmin
# from xadmin.views import BaseAdminPlugin, ListAdminView
# from django.template import loader
#
#
# #excel导入
# class ListImportExcelPlugin(BaseAdminPlugin):
#     import_excel = True
#
#     def init_request(self, *args, **kwargs):
#         return bool(self.import_excel)
#
#     def block_top_toolbar(self, context, nodes):
#         nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html'))
#
# xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)