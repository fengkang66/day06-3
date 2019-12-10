import requests

import api


class ApiEmployee:
    def __init__(self):
        # 添加员工
        self.url_add = api.BASE_URL + "/api/sys/user"
        self.url_employee = api.BASE_URL + "/api/sys/user/{}"

# 添加员工

    def api_post_employee(self,username,mobile,workNumber):
       # 定义json数据
        data = {"username":username,
                "mobile":mobile,
                "workNumber":workNumber}
        return requests.post(url=self.url_add,json=data,headers=api.headers)




    def api_put_employee(self):

        pass

    def api__get_employee(self):
        pass




    def api__delete_employee(self,user_id):
        return requests.delete(url=self.url_employee.format(user_id),headers=api.headers)
