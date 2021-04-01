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
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def param_sort(param1, param2):
    """
    :param param1:列表或者是一个元组
    :param param2:列表或者是一个元组
    :return:固定返回参数1一定是值多的那个，参数2一定是值少的那个
    """
    if type(param1) in (list, tuple) and type(param2) in (list, tuple):
        if len(param1) <= len(param2):
            return param2, param1
        else:
            return param1, param2
    else:
        print("参数类型要是列表或者是元组")
        return False


# 笛卡尔积
"""
1234567
123
用例：11,22,33,41,52
"""


# 思路：1.先找到哪个参数值多
#      2.算出参数值多的长度是参数值少的多少倍，余数是多少
#      3.按照倍数扩充参数值少的那个（新1），按照余数取出值少的参数的前几位元素值（新2）
#      4.拼接新1和新2
def create_cases(param1, param2):
    param1, param2 = param_sort(param1, param2)
    result = []
    # 取整
    n1 = len(param1) // len(param2)
    # 取余
    n2 = len(param1) % len(param2)
    param2_new = param2 * n1
    if n2 > 1:
        for i in range(n2):
            param2_new += [param2[i]]
    else:
        param2_new += [param2[0]]
    # 当原始参数1和2一样长的时候，此时扩充后的参数2会多一位，需注意按照参数1的长度进行遍历
    for i in range(len(param1)):
        result.append([param1[i], param2_new[i]])
    return result


l = [1, 2, 3]
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(create_cases(l, l1))
