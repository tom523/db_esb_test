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
from django.db.backends.mysql.base import IntegrityError
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from account.decorators import login_exempt
from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
from common.log import logger
from home_application.models import MenuVersion
from test_application.models import NewVersionLog
import random, datetime
import json

def home(request):
    # from blueking.component.shortcuts import get_client_by_request
    # client = get_client_by_request(request)
    # kwargs = {}
    # result = client.cc.search_business(kwargs)
    # return render_mako_context(request, '/test_application/index_magic.html', {
    #     "menu_version": result.get('data').get('info')
    # })
    return render_mako_context(request, '/test_application/new_version.html', {})

# @login_exempt
# @csrf_exempt
def test(request):
    return render_json({
        "result": True,
    })

def new_version(request):
    # store_id_list = request.GET.get('store_ids').split(',')
    # logger.info(u"发版前的检查：" + str(store_id_list))
    return render_mako_context(request, '/test_application/new_version.html', {})


def check_storeids(request):
    store_id_list = request.GET.getlist('data[]')
    items_list = []
    for i in range(len(store_id_list)):
        item = {
            "index": i,
            "columnName1": store_id_list[i],
            "columnName2": u"门店名称",
            "columnName3": random.choice([u'通过', u'不通过']),
            "columnName4": random.choice([u'通过', u'不通过']),
        }
        item['isOk'] = u'通过' if item['columnName3'] == u'通过' and item['columnName4'] == u'通过' else u'不通过',

        items_list.append(item)

    rtdata = {
        "catalogues":{
            "index": u"序号",
            "task": u"门店ID",
            "progress": u"门店名称",
            "host": u"检查项1",
            "date": u"检查项2",
        },
        "items":items_list,
    }
    return render_json(rtdata)


def change_version(request):
    return render_mako_context(request, '/test_application/change_version.html', {})


# 发版操作
def new_menu(request):
    items_unicode = request.GET.get('data')
    items_list = json.loads(items_unicode)
    for item in items_list:
        NewVersionLog.objects.create(
            storeid=item['id'],
            storename=item['name'],
            create_time=datetime.datetime.now(),
            menu_version=MenuVersion.objects.get(id = int(item['menu_version_id'])),
            oper_type=u"发版",
            oper_user=request.user.username,
        )
    # duplicated_store = {}
    # success_store = {}
    # fail_store = {}
    # for item in items_list:
    #     try:
    #         if item['isOk'][0] == u'不通过':
    #             NewVersionLog.objects.create(
    #                 storeid = item['columnName1'],
    #                 storename = item['columnName2'],
    #                 create_time = datetime.datetime.now(),
    #                 menu_version=MenuVersion.objects.get(id = int(item['menu_version_id'])),
    #                 success=False,
    #             )
    #             fail_store[item['columnName1']] = item['columnName2']
    #         elif item['isOk'][0] == u"通过":
    #             NewVersionLog.objects.create(
    #                 storeid=item['columnName1'],
    #                 storename=item['columnName2'],
    #                 create_time=datetime.datetime.now(),
    #                 menu_version=MenuVersion.objects.get(id = int(item['menu_version_id'])),
    #                 success=True,
    #             )
    #             success_store[item['columnName1']] = item['columnName2']
    #         else:
    #             return render_json({
    #                 "code": 10,
    #                 "message": "unknown error",
    #                 "data": "",
    #             })
    #     except Exception, e:
    #         if(e[0] == 1062):
    #             duplicated_store[item['columnName1']] = item['columnName2']

    return render_json({
        "code": 0,
        "message": "",
        "data": "",
    })


def get_menu_version(request):
    menu = {}
    for mv in MenuVersion.objects.all():
        menu[mv.id]=mv.menu_cn_name
    return render_json({
        "code": 0,
        "message": "",
        "data": menu,
    })


def get_new_version_success(request):
    retdata = []
    for item in NewVersionLog.objects.filter(success=True):
        retdata.append({
            "storeid": item.storeid,
            "storename": item.storename,
            "create_time": item.create_time.strftime("%Y-%m-%d"),
            "menu_version": MenuVersion.objects.get(id = item.menu_version_id).menu_cn_name,
        })
    return render_json({"data": retdata})




def get_new_version_fail(request):
    retdata = []
    for item in NewVersionLog.objects.filter(success=False):
        retdata.append({
            "storeid": item.storeid,
            "storename": item.storename,
            "create_time": item.create_time.strftime("%Y-%m-%d"),
            "menu_version": MenuVersion.objects.get(id = item.menu_version_id).menu_cn_name,
        })
    return render_json({"data": retdata})


def del_new_version_log(request):
    store_ids = request.GET.getlist('data[]')
    NewVersionLog.objects.filter(storeid__in=store_ids).delete()
    return render_json({
        "code": 0,
        "message": "",
        "data": "",
    })


def change_version_query_store(request):
    store_id_list = request.GET.getlist('data[]')
    o_vsn_id = request.GET.get('o_vsn_id')
    n_vsn_id = request.GET.get('n_vsn_id')
    items_list = []
    for i in range(len(store_id_list)):
        item = {
            "index": i,
            "id": store_id_list[i],
            "name": u"门店名称",
            "o_vsn": MenuVersion.objects.get(id=o_vsn_id).menu_cn_name,
            "n_vsn": MenuVersion.objects.get(id=n_vsn_id).menu_cn_name,
        }

        items_list.append(item)

    rtdata = {
        "catalogues":{
            "index": u"序号",
            "id": u"门店ID",
            "name": u"门店名称",
            "o_vsn": u"原菜单",
            "n_vsn": u"新菜单",
        },
        "items":items_list,
    }
    return render_json(rtdata)


def base_version(request):
    return render_mako_context(request, '/test_application/base_version.html', {})


# 使用datatable后的发版前检查表格的数据
def get_store_check_result(request):
    store_id_list = request.GET.get('store_ids').split(',')
    items_list = []
    for i in range(len(store_id_list)):
        item = {
            "name": u"门店名称",
            "id": store_id_list[i],
            "check1": random.choice([u'通过', u'不通过']),
            "check2": random.choice([u'通过', u'不通过']),
            "check3": random.choice([u'通过', u'不通过']),
            "check4": random.choice([u'通过', u'不通过']),
        }
        item['isOk'] = u'通过' if \
                           item['check1'] == u'通过' and \
                           item['check2'] == u'通过' and \
                           item['check3'] == u'通过' and \
                           item['check4'] == u'通过' else u'不通过',

        items_list.append(item)
    return render_json({"data": items_list})


def get_new_version_log(request):
    retdata = []
    for item in NewVersionLog.objects.all():
        retdata.append({
            "id": item.storeid,
            "name": item.storename,
            "create_time": item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "menu_version": MenuVersion.objects.get(id = item.menu_version_id).menu_cn_name,
            "oper_type": item.oper_type,
            "oper_user": item.oper_user,
        })
    return render_json({"data": retdata})


def base_version_query_store(request):
    store_id = request.GET.getlist('data')
    items = [{
        "index": 1,
        "id": store_id,
        "name": u"门店名称",
        "tbl1": "211",
        "tbl2": "232",
        "tbl3": "232",
    }]

    rtdata = {
        "catalogues":{
            "index": u"序号",
            "id": u"门店ID",
            "name": u"门店名称",
            "tbl1": u"表1",
            "tbl2": u"表2",
            "tbl3": u"表3",
        },
        "items":items,
    }
    return render_json(rtdata)