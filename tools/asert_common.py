def assert_common(self,response,status_code=200):

    # 状态码、
    self.assertEqual(status_code,response.status_code)


   # 断言success、
    self.assertTrue(response.json().get("success"))



   # code
    self.assertEqual(10000,response.json().get("code"))

    # msg
    self.assertEqual("操作成功！",response.json().get("message"))