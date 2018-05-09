# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

# import from apps here


# import from lib
# ===============================================================================
# from django.contrib import admin
# from apps.__.models import aaaa
#
# admin.site.register(aaaa)
# ===============================================================================
from django.contrib import admin
from .models import MenuVersionOnlineProduct, MenuVersion, MenuVersionCategoryItem, MenuVersionReplaceProduct


class MenuVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_cn_name')


class MenuVersionOnlineProductAdmin(admin.ModelAdmin):
    list_display = ('STORE_CODE', 'POS_CODE', 'ONLINE_SHOW_CN_NAME','MENU_VERSION')
    list_editable = ('ONLINE_SHOW_CN_NAME', 'MENU_VERSION')
    list_filter = ('MENU_VERSION', 'SALE_CHANNEl', 'DEL_FLAG', 'POS_CODE')


class MenuVersionCategoryItemAdmin(admin.ModelAdmin):
    list_display = ('STORE_CODE', 'MENU_CODE', 'PRODUCT_ITEM_CODE','MENU_VERSION')
    list_filter = ('MENU_VERSION', 'SALE_CHANNEl', 'DEL_FLAG', 'PRODUCT_ITEM_CODE')



class MenuVersionReplaceProductAdmin(admin.ModelAdmin):
    list_display = ('STORE_CODE', 'COMBO_CODE', 'PRODUCT_CODE','MENU_VERSION')
    list_filter = ('MENU_VERSION', 'SALE_CHANNEl', 'DEL_FLAG', 'COMBO_CODE')

# admin.site.register([MenuVersionOnlineProduct, MenuVersion, MenuVersionCategoryItem, MenuVersionReplaceProduct], admin_class=[MenuVersionAdmin,MenuVersionOnlineProductAdmin])
# admin.site.register(MenuVersion)
admin.site.register(MenuVersionOnlineProduct, admin_class=MenuVersionOnlineProductAdmin)
admin.site.register(MenuVersion, admin_class=MenuVersionAdmin)
admin.site.register(MenuVersionCategoryItem, admin_class=MenuVersionCategoryItemAdmin)
admin.site.register(MenuVersionReplaceProduct, admin_class=MenuVersionReplaceProductAdmin)