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

def home(request):
    return render_mako_context(request, '/test_application/index_magic.html', {})


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

    rtdata = {
        "catalogues":{
            "index": u"序号",
            "task": u"门店ID",
            "progress": u"门店名称",
            "host": u"检查项1",
            "date": u"检查项2",
        },
        "items":[
            {
                "index": 1,
                "columnName1": "111111",
                "columnName2": u"门店名称1",
                "columnName3": u"通过",
                "columnName4": u"通过",
                "isOk": 1,
            },
            {
                "index": 1,
                "columnName1": "222222",
                "columnName2": u"门店名称1",
                "columnName3": u"通过",
                "columnName4": u"通过",
                "isOk": 1,
            },
            {
                "index": 3,
                "columnName1": "222222",
                "columnName2": u"门店名称1",
                "columnName3": u"未通过",
                "columnName4": u"通过",
                "isOk": 0,
            },
        ]
    }
    return render_json(rtdata)