# 使用fixture返回一个随机数
import random
import pytest


"""
@pytest.fixture(scope="module")
def get_random():
    print("开始测试！")
    num = random.randint(1, 100)
    yield num
    print("结束测试！")
    return num
"""


# params是一个列表
@pytest.fixture(scope="module", params=[random.randint(1, 100)])
def get_random(request):
    print("开始测试！")
    yield request.param
    print("结束测试！")
    return request.param


def pytest_collection_modifyitems(session, config, items):
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

