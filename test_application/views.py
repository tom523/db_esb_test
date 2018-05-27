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
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from account.decorators import login_exempt
from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
from common.log import logger
from home_application.models import MenuVersion
from test_application.models import NewVersionFail, NewVersionSuccess
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
    pass


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
        item['isOk'] = u'通过' if item['columnName3'] == '通过' and item['columnName4'] == '通过' else u'不通过',

        items_list.append(item)

    rtdata = {
        "catalogues":{
            "index": u"序号",
            "task": u"门店ID",
            "progress": u"门店名称",
            "host": u"检查项1",
            "date": u"检查项2",
        },
        "items":items_list
    }
    return render_json(rtdata)


def change_version(request):
    pass


# 发版操作
def new_menu(request):
    items_unicode = request.GET.get('data')
    items_list = json.loads(str(items_unicode))
    for item in items_list:
        if item['isOk'][0] == '不通过':
            NewVersionFail.objects.create(
                storeid = item['columnName1'],
                storename = item['columnName2'],
                create_time = datetime.datetime.now(),
                menu_version=MenuVersion.objects.get(id = item['menu_version_id']),
            )
        elif item['isOk'][0] == "通过":
            NewVersionSuccess.objects.create(
                storeid=item['columnName1'],
                storename=item['columnName2'],
                create_time=datetime.datetime.now(),
                menu_version=MenuVersion.objects.get(id=item['menu_version_id']),
            )
        else:
            return render_json({
                "code": 10,
                "message": "unknown error",
                "data": "",
            })
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



