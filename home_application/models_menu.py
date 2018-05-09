# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class MasterMcTComboReplaceProduct(models.Model):
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=12)  # Field name made lowercase.
    store_code = models.CharField(db_column='STORE_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    combo_code = models.CharField(db_column='COMBO_CODE', max_length=12)  # Field name made lowercase.
    product_code = models.CharField(db_column='PRODUCT_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    group_code = models.BigIntegerField(db_column='GROUP_CODE', blank=True, null=True)  # Field name made lowercase.
    brand_code = models.DecimalField(db_column='BRAND_CODE', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sale_channel = models.CharField(db_column='SALE_CHANNEl', max_length=3, blank=True, null=True)  # Field name made lowercase.
    create_id = models.CharField(db_column='CREATE_ID', max_length=12)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    update_id = models.CharField(db_column='UPDATE_ID', max_length=12)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME')  # Field name made lowercase.
    del_flag = models.CharField(db_column='DEL_FLAG', max_length=3)  # Field name made lowercase.
    price_range = models.DecimalField(db_column='PRICE_RANGE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'master_mc_t_combo_replace_product'

    def __unicode__(self):
        return self.combo_code


class MasterMcTMenuCategoryItem(models.Model):
    guid = models.CharField(db_column='GUID', max_length=12)  # Field name made lowercase.
    store_code = models.CharField(db_column='STORE_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    menu_code = models.CharField(db_column='MENU_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    product_item_code = models.CharField(db_column='PRODUCT_ITEM_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    brand_code = models.DecimalField(db_column='BRAND_CODE', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    product_sort_code = models.BigIntegerField(db_column='product_Sort_Code', blank=True, null=True)  # Field name made lowercase.
    sale_channel = models.CharField(db_column='SALE_CHANNEl', max_length=3, blank=True, null=True)  # Field name made lowercase.
    create_id = models.CharField(db_column='CREATE_ID', max_length=12)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    update_id = models.CharField(db_column='UPDATE_ID', max_length=12)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME')  # Field name made lowercase.
    del_flag = models.CharField(db_column='DEL_FLAG', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'master_mc_t_menu_category_item'


class MasterMcTOnlineProduct(models.Model):
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=12)  # Field name made lowercase.
    brand_code = models.DecimalField(db_column='BRAND_CODE', max_digits=4, decimal_places=0)  # Field name made lowercase.
    store_code = models.CharField(db_column='STORE_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pos_code = models.CharField(db_column='POS_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sales_min_num = models.BigIntegerField(db_column='SALES_MIN_NUM', blank=True, null=True)  # Field name made lowercase.
    sales_max_num = models.BigIntegerField(db_column='SALES_MAX_NUM', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sales_start_time = models.DateTimeField(db_column='SALES_START_TIME', blank=True, null=True)  # Field name made lowercase.
    sales_end_time = models.DateTimeField(db_column='SALES_END_TIME', blank=True, null=True)  # Field name made lowercase.
    sales_time_part = models.CharField(db_column='SALES_TIME_PART', max_length=33, blank=True, null=True)  # Field name made lowercase.
    sales_special_time = models.CharField(db_column='SALES_SPECIAL_TIME', max_length=33, blank=True, null=True)  # Field name made lowercase.
    is_week_sales = models.CharField(db_column='IS_WEEK_SALES', max_length=2, blank=True, null=True)  # Field name made lowercase.
    online_show_cn_name = models.CharField(db_column='ONLINE_SHOW_CN_NAME', max_length=166, blank=True, null=True)  # Field name made lowercase.
    online_show_en_name = models.CharField(db_column='ONLINE_SHOW_EN_NAME', max_length=16, blank=True, null=True)  # Field name made lowercase.
    picture_path = models.CharField(db_column='PICTURE_PATH', max_length=66, blank=True, null=True)  # Field name made lowercase.
    picture_alt = models.CharField(db_column='PICTURE_ALT', max_length=85, blank=True, null=True)  # Field name made lowercase.
    produce_online_price = models.DecimalField(db_column='PRODUCE_ONLINE_PRICE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    is_wechat_room_sales = models.CharField(db_column='IS_WECHAT_ROOM_SALES', max_length=3, blank=True, null=True)  # Field name made lowercase.
    is_wechat_delivery_sales = models.CharField(db_column='IS_WECHAT_DELIVERY_SALES', max_length=3, blank=True, null=True)  # Field name made lowercase.
    is_online_property = models.CharField(db_column='IS_ONLINE_PROPERTY', max_length=3, blank=True, null=True)  # Field name made lowercase.
    is_member_sale = models.CharField(db_column='IS_MEMBER_SALE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sale_channel = models.CharField(db_column='SALE_CHANNEl', max_length=3, blank=True, null=True)  # Field name made lowercase.
    product_cn_description = models.CharField(db_column='PRODUCT_CN_DESCRIPTION', max_length=85, blank=True, null=True)  # Field name made lowercase.
    product_en_description = models.CharField(db_column='PRODUCT_EN_DESCRIPTION', max_length=85, blank=True, null=True)  # Field name made lowercase.
    product_online_shortname = models.CharField(db_column='PRODUCT_ONLINE_SHORTNAME', max_length=16, blank=True, null=True)  # Field name made lowercase.
    create_id = models.CharField(db_column='CREATE_ID', max_length=12)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    update_id = models.CharField(db_column='UPDATE_ID', max_length=12)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME')  # Field name made lowercase.
    del_flag = models.CharField(db_column='DEL_FLAG', max_length=3)  # Field name made lowercase.
    picture_name = models.CharField(db_column='PICTURE_NAME', max_length=33, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    vip_discount = models.IntegerField(db_column='VIP_DISCOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'master_mc_t_online_product'
