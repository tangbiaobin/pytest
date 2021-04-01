# 企业微信接口
import requests
from requests import Session
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
            "fetch_child": 4
        }
        req = requests.get(url=url, params=data)
        print(req.json())
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


class UserBase:

    def __init__(self, token_url, corp_id, corp_secret):
        self.url = token_url
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.s = Session()
        self.token = self.get_token(self.url)

    # 获取token
    def get_token(self, url):
        data = {
            "corpid": self.corp_id,
            "corpsecret": self.corp_secret
        }
        req = self.s.get(self.url, params=data)
        return req.json()['access_token']

    # 查询成员
    def get_user(self, user_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        data = {
            "access_token": self.token,
            "userid": user_id
        }
        req = self.s.get(url, params=data)
        return req.json()

    # 添加成员
    def create_user(self, userid, name, department, mobile, gender, email, position):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile,
            "gender": gender,
            "email": email,
            "position": position
        }
        req = self.s.post(url=url, json=data)
        return req.json()

    # 删除成员
    def delete_user(self, userid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        data = {
            "access_token": self.token,
            "userid": userid
        }
        req = self.s.get(url, params=data)
        return req.json()


if __name__ == "__main__":
    data = {}
    # w = WeWork()
    # w.create_user('test10', '测试10', [3], '17610001010', '2', 'test10@fangdd.com', '工程师')
    # w.create_user('test03', '测试3', [3], '17610001003', '1', 'test03@fangdd.com', '工程师')
    # w.get_users()
    # w.update_user({"access_token": w.get_token(), "userid": "test10", "external_position": "测试学员10"})
    # w.update_user({"access_token": w.get_token(), "userid": "test04", "enable": 0})
    # for user in w.get_users():
    #     if "external_position" in user.keys():
    #         if user["external_position"] == "测试学员":
    #             data['userid'] = user['userid']
    #             w.delete_user({"access_token": w.get_token(), "userid": data['userid']})
    # w.get_users()
    # s = Session()
    # print(dir(s))
    u = UserBase("https://qyapi.weixin.qq.com/cgi-bin/gettoken", "wwb1f41b9d378f61a6",
                 "fCco872UfsJ31LozgFcefF5jzW-wNx0_RrSvmSwdSDU")
    print(u.get_user('test13'))
    # print(u.delete_user('test13'))
