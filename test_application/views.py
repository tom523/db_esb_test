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


def home(request):
    return render_mako_context(request, '/test_application/index.html', {})


# @login_exempt
# @csrf_exempt
def test(request):
    return render_json({
        "result": True,
    })









