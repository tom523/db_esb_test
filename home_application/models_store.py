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


class City(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    citycode = models.CharField(db_column='CityCode', max_length=20)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=50)  # Field name made lowercase.
    zoneno = models.CharField(db_column='ZoneNo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    isneedsyn = models.IntegerField(db_column='isNeedSyn', blank=True, null=True)  # Field name made lowercase.
    hdsid = models.CharField(db_column='hdsId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cityname_zh = models.CharField(db_column='CityName_zh', max_length=50)  # Field name made lowercase.
    needinvoicetitle = models.IntegerField(db_column='needInvoiceTitle', blank=True, null=True)  # Field name made lowercase.
    onlineordering = models.IntegerField(db_column='onlineOrdering', blank=True, null=True)  # Field name made lowercase.
    abbr = models.CharField(max_length=20, blank=True, null=True)
    marketcode = models.CharField(db_column='marketCode', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class District(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    districtcode = models.CharField(db_column='DistrictCode', max_length=20)  # Field name made lowercase.
    districtname = models.CharField(db_column='DistrictName', max_length=50)  # Field name made lowercase.
    ascity = models.IntegerField(db_column='asCity', blank=True, null=True)  # Field name made lowercase.
    pinyinname = models.CharField(db_column='pinyinName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    abbr = models.CharField(max_length=20, blank=True, null=True)
    citycode = models.CharField(db_column='cityCode', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'district'


class Market(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    marketcode = models.CharField(db_column='MarketCode', unique=True, max_length=20)  # Field name made lowercase.
    marketname = models.CharField(db_column='MarketName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'market'


class Store(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    storecode = models.CharField(db_column='StoreCode', max_length=10)  # Field name made lowercase.
    finstorecode = models.CharField(db_column='FinStoreCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cxjstorecode = models.CharField(db_column='CXJStoreCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=50)  # Field name made lowercase.
    storeaddresspy = models.CharField(db_column='StoreAddressPy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  # Field name made lowercase.
    districtcode = models.CharField(db_column='DistrictCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=150, blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    property = models.CharField(db_column='Property', max_length=1, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    delivery = models.IntegerField(db_column='Delivery', blank=True, null=True)  # Field name made lowercase.
    traffic = models.CharField(db_column='Traffic', max_length=100, blank=True, null=True)  # Field name made lowercase.
    posversion = models.CharField(db_column='PosVersion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    isused = models.IntegerField(db_column='IsUsed', blank=True, null=True)  # Field name made lowercase.
    storetype = models.IntegerField(db_column='storeType', blank=True, null=True)  # Field name made lowercase.
    enableemail = models.IntegerField(db_column='enableEmail', blank=True, null=True)  # Field name made lowercase.
    menuversion = models.CharField(db_column='MenuVersion', max_length=38, blank=True, null=True)  # Field name made lowercase.
    rapversion = models.CharField(db_column='RapVersion', max_length=38, blank=True, null=True)  # Field name made lowercase.
    posmenuversion = models.CharField(db_column='PosMenuVersion', max_length=46, blank=True, null=True)  # Field name made lowercase.
    posrapversion = models.CharField(db_column='PosRapVersion', max_length=46, blank=True, null=True)  # Field name made lowercase.
    lastmenuserial = models.CharField(db_column='LastMenuSerial', max_length=36, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    deliverytime = models.SmallIntegerField(db_column='DeliveryTime', blank=True, null=True)  # Field name made lowercase.
    businessdate = models.DateTimeField(db_column='BusinessDate', blank=True, null=True)  # Field name made lowercase.
    forcesendbyemail = models.IntegerField(db_column='ForceSendByEmail', blank=True, null=True)  # Field name made lowercase.
    shutreason = models.CharField(db_column='ShutReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    merchantno = models.CharField(db_column='Merchantno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(max_length=10, blank=True, null=True)
    endtime = models.CharField(max_length=10, blank=True, null=True)
    opentype = models.CharField(db_column='OpenType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    opendate = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    openonlinepay = models.IntegerField(db_column='openOnlinePay', blank=True, null=True)  # Field name made lowercase.
    abbr = models.CharField(max_length=20, blank=True, null=True)
    shutmaptime = models.IntegerField(db_column='ShutMapTime', blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    rgm = models.CharField(db_column='RGM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    am = models.CharField(db_column='AM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dm = models.CharField(db_column='DM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iscall = models.CharField(db_column='isCall', max_length=1, blank=True, null=True)  # Field name made lowercase.
    coordinate_x = models.CharField(max_length=20, blank=True, null=True)
    coordinate_y = models.CharField(max_length=20, blank=True, null=True)
    repairorderemail = models.CharField(db_column='repairOrderEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ishui = models.IntegerField(db_column='isHui', blank=True, null=True)  # Field name made lowercase.
    iseinvoice = models.CharField(db_column='isEInvoice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isinvoicetitle = models.CharField(db_column='isInvoiceTitle', max_length=1)  # Field name made lowercase.
    outofinvoice = models.IntegerField(db_column='outofInvoice', blank=True, null=True)  # Field name made lowercase.
    storetypes = models.CharField(db_column='storeTypes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    channelid = models.CharField(db_column='channelId', max_length=20)  # Field name made lowercase.
    appkey = models.CharField(db_column='appKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    appsecret = models.CharField(db_column='appSecret', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postype = models.CharField(db_column='posType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isenclosing = models.IntegerField(db_column='isEnclosing', blank=True, null=True)  # Field name made lowercase.
    deliveryprice = models.CharField(db_column='deliveryPrice', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'

    def __unicode__(self):
        return self.storename


class TBiBanner(models.Model):
    bannerid = models.IntegerField(primary_key=True)
    bannertype = models.IntegerField(blank=True, null=True)
    imageurl = models.CharField(db_column='imageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    relationtype = models.IntegerField(db_column='relationType', blank=True, null=True)  # Field name made lowercase.
    linkedclassid = models.CharField(db_column='linkedClassid', max_length=10, blank=True, null=True)  # Field name made lowercase.
    linkedurl = models.CharField(db_column='linkedUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    validfrom = models.DateTimeField(blank=True, null=True)
    validto = models.DateTimeField(blank=True, null=True)
    desccn = models.CharField(db_column='descCn', max_length=500, blank=True, null=True)  # Field name made lowercase.
    descen = models.CharField(db_column='descEn', max_length=500, blank=True, null=True)  # Field name made lowercase.
    showorder = models.IntegerField(db_column='showOrder', blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    market = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    smallpictureurl = models.CharField(db_column='smallPictureUrl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispopup = models.CharField(db_column='isPopup', max_length=1, blank=True, null=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='versionId', blank=True, null=True)  # Field name made lowercase.
    holiday = models.CharField(max_length=1, blank=True, null=True)
    dayofweek = models.CharField(db_column='dayOfWeek', max_length=100, blank=True, null=True)  # Field name made lowercase.
    channelid = models.CharField(db_column='channelId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titlecn = models.CharField(db_column='titleCn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titleen = models.CharField(db_column='titleEn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    briefcn = models.CharField(db_column='briefCn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    briefen = models.CharField(db_column='briefEn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    altdesc = models.CharField(db_column='altDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cityselecttype = models.IntegerField(db_column='citySelectType', blank=True, null=True)  # Field name made lowercase.
    stypes = models.CharField(max_length=200, blank=True, null=True)
    exceptstore = models.CharField(db_column='exceptStore', max_length=15000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_bi_banner'
