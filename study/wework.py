# 企业微信接口
import requests
import json


class WeWork:

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data = {
            "corpid": "wwb1f41b9d378f61a6",
            "corpsecret": "fCco872UfsJ31LozgFcefF5jzW-wNx0_RrSvmSwdSDU"
        }
        req = requests.get(url=url, params=data)
        return req.json()['access_token']

    def create_depart(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.get_token()}"
        data = {
            "name": "唐彪斌",
            "name_en": "tbb",
            "parentid": 1
        }
        req = requests.post(url=url, json=data)
        # return req.json()['id']

    def get_depart(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        data = {
            'access_token': self.get_token()
        }
        req = requests.get(url=url, params=data)
        print(req.json())

    def delete_depart(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        data = {
            'access_token': self.get_token(),
            "id": 4
        }
        req = requests.get(url=url, params=data)
        print(req.json())

    def create_user(self, userid="", name="", department=[], mobile="", gender="", email="", position=""):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token()}"
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile,
            "gender": gender,
            "email": email,
            "position": position
        }
        req = requests.post(url=url, json=data)
        print(req.json())

    def get_users(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/list"
        data = {
            "access_token": self.get_token(),
            "department_id": 3,
            "fetch_child": 1
        }
        req = requests.get(url=url, params=data)
        # print(req.json())
        return req.json()['userlist']

    def update_user(self, data):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.get_token()}"
        if type(data) is dict:
            req = requests.post(url=url, json=data)
            print("----------")
            print(req.json())
        else:
            print("参数格式不是字典")

    def delete_user(self, data):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        req = requests.get(url=url, params=data)
        print(req.json())


if __name__ == "__main__":
    data = {}
    w = WeWork()
    # w.create_user('test02', '测试2', [3], '17610001002', '2', 'test02@fangdd.com', '工程师')
    # w.create_user('test03', '测试3', [3], '17610001003', '1', 'test03@fangdd.com', '工程师')
    # w.get_users()
    # w.update_user({"access_token": w.get_token(), "userid": "test05", "external_position": "测试学员"})
    # w.update_user({"access_token": w.get_token(), "userid": "test04", "enable": 0})
    for user in w.get_users():
        if "external_position" in user.keys():
            if user["external_position"] == "测试学员":
                data['userid'] = user['userid']
                w.delete_user({"access_token": w.get_token(), "userid": data['userid']})
    w.get_users()
