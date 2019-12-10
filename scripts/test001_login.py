import unittest

import api

from api.api_login import ApiLogin
from tools.asert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):

        cls.login = ApiLogin()

# 登录测试方法
    def test_login01(self,mobile="13800000002",password="123456"):
        # 调用业务方法
        r = self.login.api_login(mobile,password)
        # 提取token
        token = r.json().get("data")
        api.headers["Authorization"] = "Bearer " + token
        print("登录成功后的headers值为：",api.headers)
        print(r.json())
        # 断言
        assert_common(self,r)