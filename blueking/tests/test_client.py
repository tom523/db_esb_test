# -*- coding: utf-8 -*-
import json
from django.test import TestCase

from blueking.component import client, collections


class TestCLIENT(TestCase):

    def setUp(self):
        client.BaseComponentClient.setup_components(collections.AVAILABLE_COLLECTIONS)
        client.ComponentClientWithSignature.setup_components(collections.AVAILABLE_COLLECTIONS)
        self.app_code = 'esb_test'
        self.app_secret = 'secret12345'

    def test_signature_client(self):
        base_client = client.ComponentClientWithSignature(self.app_code, self.app_secret)
        params_list = [
            {
                'bk_username': 'admin',
                'app_id': 2,
            }
        ]
        bk_api_ver = 'v2'
        for params in params_list:
            base_client.set_bk_api_ver(bk_api_ver)
            result = base_client.cc.get_app_by_id(params)
            print json.dumps(result)

    def test_base_client(self):
        base_client = client.BaseComponentClient(self.app_code, self.app_secret)
        params_list = [
            {
                'bk_username': 'admin',
                'app_id': 2,
            }
        ]
        for params in params_list:
            result = base_client.cc.get_app_by_id(params)
            print json.dumps(result)
