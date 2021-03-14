# coding=utf-8
import pytest
from study.calculator import Calculator
import json


"""
本次练习1
使用【测试数据的数据驱动】的方法完成加减乘除测试
1、从yml文件中读取所有测试用例，（至少有一个用例失败后重跑2次，设置每个用例的执行顺序，是用例按顺序执行，至少一个用例有多个断言，一个断言失败后能继续执行后面的断言）
2、将fixture方法放在conftest.py里面，设置scope=module，从fixture中返回一个随机数，在测试用例中获取这个随机数并打印出来，开始测试前打印开始测试，所有用例执行完成后打印用例执行完成
3、修改运行规则pytest.ini文件，使默认执行pytest时，自动带上sv参数，只执行以test开始的文件
4、在测试用例中增加中文信息，如用例的ids以中文命名，并且能够在执行时正常显示出来
5、通过程序控制将所有用例倒序执行
6、执行完成后能够生成测试报告
"""


# 封装读取json数据的方法
def get_data(file_name=''):
    if file_name:
        path = 'D:/code/pytest/data/' + file_name
        with open(path) as f:
            data = json.load(f)
            return data
    else:
        print('请输入参数文件！')


# 使用【测试数据的数据驱动】的方法完成加减乘除测试
class TestCalculator:

    def setup_class(self):
        print("开始计算")
        self.c = Calculator()

    def teardown_class(self):
        print("结束计算")

    # 加
    # 这种参数化时值为list类型，若是dict类型则只取字典中的key
    @pytest.mark.parametrize('a,b, exc', get_data("data.json")['param']["add"], ids=get_data("data.json")["ids"]["add"])
    # 失败重跑,设置重跑次数为2，延迟1s
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    # 设置用例执行顺序
    @pytest.mark.run(order=1)
    def test_add(self, a, b, exc):
        result = self.c.add(a, b)
        # 设置多个断言:当设置多个断言时&失败重跑，只要存在断言失败即重跑
        pytest.assume(result == exc)
        pytest.assume(result)

    # 减
    @pytest.mark.parametrize('a,b, exc', get_data('data.json')["param"]['minus'])
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.run(order=2)
    def test_minus(self, a, b, exc):
        result = self.c.minus(a, b)
        assert result == exc

    # 除
    @pytest.mark.parametrize('a,b, exc', get_data('data.json')["param"]['divide'])
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.run(order=4)
    def test_divide(self, a, b, exc):
        if b != 0:
            result = self.c.divide(a, b)
            assert result == exc
        else:
            print("除数不能为0")

    # 乘
    @pytest.mark.parametrize('a,b, exc', get_data('data.json')["param"]['mul'])
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.run(order=3)
    def test_multiple(self, a, b, exc):
        result = self.c.multiple(a, b)
        assert result == exc


class TestCalculator1:

    def setup_class(self):
        print("开始计算")
        self.c = Calculator()

    def teardown_class(self):
        print("结束计算")

    # 加
    # 这种参数化时值为list类型，若是dict类型则只取字典中的key
    @pytest.mark.parametrize('a,b, exc', get_data("data.json")['param']["add"], ids=get_data("data.json")["ids"]["add"])
    # 失败重跑,设置重跑次数为2，延迟1s
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_add(self, a, b, exc):
        result = self.c.add(a, b)
        # 设置多个断言:当设置多个断言时&失败重跑，只要存在断言失败即重跑
        pytest.assume(result == exc)
        pytest.assume(result)

    # 减
    @pytest.mark.parametrize('a,b, exc', get_data('data.json')["param"]['minus'])
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_minus(self, a, b, exc):
        result = self.c.minus(a, b)
        assert result == exc

    # 除
    @pytest.mark.parametrize('a,b, exc', get_data('data.json')["param"]['divide'])
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_divide(self, a, b, exc):
        if b != 0:
            result = self.c.divide(a, b)
            assert result == exc
        else:
            print("除数不能为0")

    # 乘
    @pytest.mark.parametrize('a,b, exc', get_data('data.json')["param"]['mul'])
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_multiple(self, a, b, exc):
        result = self.c.multiple(a, b)
        assert result == exc


if __name__ == "__main__":
    pytest.main(["-s", "test_cal.py"])
