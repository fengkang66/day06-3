import api
import requests

class ApiLogin:
    def __init__(self):
        self.url = api.BASE_URL+"/api/sys/login"
    def api_login(self,mobile,pssword):
        data = {"mobile":mobile,"password":pssword}
        return requests.post(url=self.url,json=data,headers=api.headers)

if __name__ == '__main__':

    a=ApiLogin()
    w=a.api_login("13512345678","123456")
    print(w.json())
