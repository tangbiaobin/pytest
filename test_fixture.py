"""
2、将fixture方法放在conftest.py里面，设置scope=module，从fixture中返回一个随机数，在测试用例中获取这个随机数并打印出来，开始测试前打印开始测试，所有用例执行完成后打印用例执行完成
4、在测试用例中增加中文信息，如用例的ids以中文命名，并且能够在执行时正常显示出来
5、通过程序控制将所有用例倒序执行
6、执行完成后能够生成测试报告
"""
import pytest


class TestFixture:

    # 获取用pytest.fixture修饰的函数的返回值时，只需要函数名，不需要()
    def test_print_random(self, get_random):
        print("test1")
        print(get_random)

    def test_print_random1(self, get_random):
        print("test2")
        print(get_random)


if __name__ == "__main__":
    pytest.main(['-sv', 'test_fixture.py'])
