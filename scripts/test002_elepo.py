import unittest

# from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from tools.asert_common import assert_common


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取 ApiEmployee对象
        cls.api = ApiEmployee()

    # 新增员工
    # @parameterized.expand(read_txt("employee_post.txt"))
    def test01_post(self,username="bj170",mobile="13012345997",workNumber="694564"):
        # 调用新街口
        r = self.api.api_post_employee(username,mobile,workNumber)
        print("新增后员工结果：",r.json())
        # 提取user-id
        api.user_id = r.json().get("data").get("id")
        print("新增员工ID为：",api.user_id)
        # 断言
        assert_common(self,r)






