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

from django.conf.urls import patterns

urlpatterns = patterns(
    'test_application.views',
    (r'^$', "home"),
    (r'^test/', "test"),
    (r'^new_version/', "new_version"),
    (r'^base_version/', "base_version"),
    (r'^new_menu/', "new_menu"),
    (r'^change_version/', "change_version"),
    (r'^check_storeids/', "check_storeids"),
    (r'^get_menu_version/$', 'get_menu_version'),
    (r'^del_new_version_log/$', 'del_new_version_log'),
    (r'^get_new_version_log/$', 'get_new_version_log'),
    (r'^get_new_version_fail/$', 'get_new_version_fail'),
    (r'^get_store_check_result/$', 'get_store_check_result'),
    (r'^change_version_query_store/$', 'change_version_query_store'),
    (r'^base_version_query_store/$', 'base_version_query_store'),

)
