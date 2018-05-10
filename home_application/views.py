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

from common.mymako import render_mako_context, render_json
from home_application.models_store import Store
from models_menu import MasterMcTComboReplaceProduct, MasterMcTOnlineProduct, MasterMcTMenuCategoryItem
from models import MenuVersionOnlineProduct, MenuVersionReplaceProduct, MenuVersion, MenuVersionCategoryItem
import time
from common.log import logger


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def get_test_data(request):
    qset = MasterMcTOnlineProduct.objects.using('dicos_menu').values('online_show_cn_name', 'pos_code').distinct()
    return render_json({
        'result': True,
        'current_time': time.strftime('%Y-%m-%d %H:%M:%S'),
        'count': len(qset),
        'data': list(qset),
        'code': 0,
        'message': "",
    })


def insert_data_to_dicos_db(request, data):
    '''
    data: {'master_mc_t_combo_replace_product': [row1, row2, row3..., rowN],
        'master_mc_t_menu_category_item': [row1, row2, row3..., rowN],
        'master_mc_t_online_product': [row1, row2, row3..., rowN]}
    :param request:
    :param data:
    :return:
    '''


def get_data_from_local_db(request):
    pass


def get_item_from_local_db(request):
    pass


# 根据多个【门店编码】和【菜单版本ID】给门店上新菜单
def new_menu_for_multiple_store(request, menu_version_id, store_codes):
    store_code_list = store_codes.split('_')
    try:
        for code in store_code_list:
            _new_menu(request, menu_version_id, store_code=code)
    except Exception, e:
        return render_json({
            "result": False,
            "code": 111,
            "message": "save data fail！！！",
            "current_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        })
    else:
        return render_json({
            "result": True,
            "code": 0,
            "message": "save data success",
            "current_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        })


# 根据单个【门店编码】和【菜单版本ID】给门店上新菜单
def new_menu(request, menu_version_id, store_code):
    '''

    :param request:
    :param menu_version_id:菜单版本ID
    :param STORE_CODE:门店编码
    :return:
    '''
    # 获取菜单版本对象
    # logger.debug(menu_version_id)
    # logger.debug(store_code)
    try:
        _new_menu(request, menu_version_id, store_code=store_code)
            # logger.info(c_item.to_MasterMcTMenuCategoryItem(store_code))

    except Exception, e:
        logger.error("get menuversion id : %s" % e)
        return render_json({
            "result": False,
            "code": 111,
            "message": "保存数据错误！！！",
            "current_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        })
    else:
        return render_json({
            "result": True,
            "code": 0,
            "message": "save data success",
            "current_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        })

    # MenuVersionOnlineProduct对象转换成MasterMcTOnlineProduct对象
    #加上GUID,去掉menu_version_id,给STORE_CODE赋值


def _new_menu(request, menu_version_id, store_code):
    m = MenuVersion.objects.filter(id=menu_version_id)
    r_querysetlist = []
    for ritem in MenuVersionReplaceProduct.objects.filter(MENU_VERSION=m):
        r_querysetlist.append(ritem.to_MasterMcTComboReplaceProduct(store_code))
        # ritem.to_MasterMcTComboReplaceProduct(store_code).save(using='test_dicos_menu')
    MasterMcTComboReplaceProduct.objects.using('dicos_menu').bulk_create(r_querysetlist)

    o_querysetlist = []
    for oitem in MenuVersionOnlineProduct.objects.filter(MENU_VERSION=m):
        o_querysetlist.append(oitem.to_MasterMcTOnlineProduct(store_code))
    MasterMcTOnlineProduct.objects.using('dicos_menu').bulk_create(o_querysetlist)
        # oitem.to_MasterMcTOnlineProduct(store_code).save(using='test_dicos_menu')

    c_querysetlist = []
    for c_item in MenuVersionCategoryItem.objects.filter(MENU_VERSION=m):
        c_querysetlist.append(c_item.to_MasterMcTMenuCategoryItem(store_code))
    MasterMcTMenuCategoryItem.objects.using('dicos_menu').bulk_create(c_querysetlist)
        # c_item.to_MasterMcTMenuCategoryItem(store_code).save(using='test_dicos_menu')



def get_storename_by_storecode(request, storecode):
    store = Store.objects.using('store_info').get(storecode=storecode)
    return store.storename


def get_menu_version(request):
    menu = {}
    for mv in MenuVersion.objects.all():
        menu[mv.id]=mv.menu_cn_name
    return render_json({
        "code": 0,
        "message": "",
        "data": menu,
    })






