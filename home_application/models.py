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

# from django.db import models
from django.db import models
import uuid
from models_menu import MasterMcTComboReplaceProduct, MasterMcTMenuCategoryItem, MasterMcTOnlineProduct


class MenuVersion(models.Model):
    menu_cn_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.menu_cn_name


class MenuVersionOnlineProduct(models.Model):

    # GUID = models.CharField(max_length=200)
    # guid在导入生产库时生成，本地数据库不需要保存
    BRAND_CODE = models.DecimalField(max_digits=4,decimal_places=0)
    STORE_CODE = models.CharField(max_length=36)
    POS_CODE = models.CharField(max_length=36, null=True)
    SALES_MIN_NUM = models.BigIntegerField(null=True)
    SALES_MAX_NUM = models.BigIntegerField(null=True)
    UNIT = models.CharField(max_length=10, null=True)
    SALES_START_TIME = models.DateTimeField(null=True)
    SALES_END_TIME = models.DateTimeField(null=True)
    SALES_TIME_PART = models.CharField(max_length=100, null=True)
    SALES_SPECIAL_TIME = models.CharField(max_length=100, null=True)
    IS_WEEK_SALES = models.CharField(max_length=7, null=True)
    ONLINE_SHOW_CN_NAME = models.CharField(max_length=500, null=True)
    ONLINE_SHOW_EN_NAME = models.CharField(max_length=50, null=True)
    PICTURE_PATH = models.CharField(max_length=200, null=True)
    PICTURE_ALT = models.CharField(max_length=255, null=True)
    PRODUCE_ONLINE_PRICE = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    IS_WECHAT_ROOM_SALES = models.CharField(max_length=1, null=True)
    IS_WECHAT_DELIVERY_SALES = models.CharField(max_length=1, null=True)
    IS_ONLINE_PROPERTY = models.CharField(max_length=1)
    IS_MEMBER_SALE = models.CharField(max_length=1, null=True)
    SALE_CHANNEl = models.CharField(max_length=1, null=True)
    PRODUCT_CN_DESCRIPTION = models.CharField(max_length=255, null=True)
    PRODUCT_EN_DESCRIPTION = models.CharField(max_length=255, null=True)
    PRODUCT_ONLINE_SHORTNAME = models.CharField(max_length=50, null=True)
    CREATE_ID = models.CharField(max_length=36)
    CREATE_TIME = models.DateTimeField()
    UPDATE_ID = models.CharField(max_length=36, null=True)
    UPDATE_TIME = models.DateTimeField()
    DEL_FLAG = models.CharField(max_length=1)
    PICTURE_NAME = models.CharField(max_length=100, null=True)
    DISCOUNT = models.IntegerField(null=True)
    VIP_DISCOUNT = models.IntegerField(null=True)
    MENU_VERSION = models.ForeignKey(MenuVersion)

    def __unicode__(self):
        return self.ONLINE_SHOW_CN_NAME + " " + self.POS_CODE + " " + self.STORE_CODE

    def to_MasterMcTOnlineProduct(self, STORE_CODE):
        return MasterMcTOnlineProduct(
            guid=uuid.uuid1(),
            brand_code=self.BRAND_CODE,
            store_code=STORE_CODE,
            pos_code=self.POS_CODE,
            sales_min_num=self.SALES_MIN_NUM,
            sales_max_num=self.SALES_MAX_NUM,
            unit=self.UNIT,
            sales_start_time=self.SALES_START_TIME,
            sales_end_time=self.SALES_END_TIME,
            sales_time_part=self.SALES_TIME_PART,
            sales_special_time=self.SALES_SPECIAL_TIME,
            is_week_sales=self.IS_WEEK_SALES,
            online_show_cn_name=self.ONLINE_SHOW_CN_NAME,
            online_show_en_name=self.ONLINE_SHOW_EN_NAME,
            picture_path=self.PICTURE_PATH,
            picture_alt=self.PICTURE_ALT,
            produce_online_price=self.PRODUCE_ONLINE_PRICE,
            is_wechat_room_sales=self.IS_WECHAT_ROOM_SALES,
            is_wechat_delivery_sales=self.IS_WECHAT_DELIVERY_SALES,
            is_online_property=self.IS_ONLINE_PROPERTY,
            is_member_sale=self.IS_MEMBER_SALE,
            sale_channel=self.SALE_CHANNEl,
            product_cn_description=self.PRODUCT_CN_DESCRIPTION,
            product_en_description=self.PRODUCT_EN_DESCRIPTION,
            product_online_shortname=self.PRODUCT_ONLINE_SHORTNAME,
            create_id=self.CREATE_ID,
            create_time=self.CREATE_TIME,
            update_id=self.UPDATE_ID,
            update_time=self.UPDATE_TIME,
            del_flag=self.DEL_FLAG,
            picture_name=self.PICTURE_NAME,
            discount=self.DISCOUNT,
            vip_discount=self.VIP_DISCOUNT,
        )


class MenuVersionCategoryItem(models.Model):
    STORE_CODE = models.CharField(max_length=36, null=True)
    MENU_CODE = models.CharField(max_length=36, null=True)
    PRODUCT_ITEM_CODE = models.CharField(max_length=36, null=True)
    BRAND_CODE = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    product_Sort_Code = models.BigIntegerField(null=True)
    SALE_CHANNEl = models.CharField(max_length=1, null=True)
    CREATE_ID = models.CharField(max_length=36)
    CREATE_TIME = models.DateTimeField()
    UPDATE_ID = models.CharField(max_length=36)
    UPDATE_TIME = models.DateTimeField()
    DEL_FLAG = models.CharField(max_length=1)
    MENU_VERSION = models.ForeignKey(MenuVersion)

    def __unicode__(self):
        return self.PRODUCT_ITEM_CODE

    def to_MasterMcTMenuCategoryItem(self, STORE_CODE):
        return MasterMcTMenuCategoryItem(
            guid=uuid.uuid1(),
            store_code=STORE_CODE,
            menu_code=self.MENU_CODE,
            product_item_code=self.PRODUCT_ITEM_CODE,
            brand_code=self.BRAND_CODE,
            product_sort_code=self.product_Sort_Code,
            sale_channel=self.SALE_CHANNEl,
            create_id=self.CREATE_ID,
            create_time=self.CREATE_TIME,
            update_id=self.UPDATE_ID,
            update_time=self.UPDATE_TIME,
            del_flag=self.DEL_FLAG,
        )


class MenuVersionReplaceProduct(models.Model):
    STORE_CODE = models.CharField(max_length=36, null=True)
    COMBO_CODE = models.CharField(max_length=36)
    PRODUCT_CODE = models.CharField(max_length=36, null=True)
    GROUP_CODE = models.BigIntegerField(null=True)
    BRAND_CODE = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    SALE_CHANNEl = models.CharField(max_length=1, null=True)
    CREATE_ID = models.CharField(max_length=36)
    CREATE_TIME = models.DateTimeField()
    UPDATE_ID = models.CharField(max_length=36)
    UPDATE_TIME = models.DateTimeField()
    DEL_FLAG = models.CharField(max_length=1)
    PRICE_RANGE = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    MENU_VERSION = models.ForeignKey(MenuVersion)

    def __unicode__(self):
        return self.COMBO_CODE

    def to_MasterMcTComboReplaceProduct(self, STORE_CODE):
        return MasterMcTComboReplaceProduct(
            guid=uuid.uuid1(),
            store_code=STORE_CODE,
            combo_code=self.COMBO_CODE,
            product_code=self.PRODUCT_CODE,
            group_code=self.GROUP_CODE,
            brand_code=self.BRAND_CODE,
            sale_channel=self.SALE_CHANNEl,
            create_id=self.CREATE_ID,
            create_time=self.CREATE_TIME,
            update_id=self.UPDATE_ID,
            update_time=self.UPDATE_TIME,
            del_flag=self.DEL_FLAG,
            price_range=self.PRICE_RANGE,
        )


class test(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name + " " + self.age


