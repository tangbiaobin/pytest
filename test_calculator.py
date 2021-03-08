import pytest
from study.calculator import Calculator


# 编写一个计算器，使用pytest，完成计算器的测试用例；使用数据驱动完成测试用例的自动生成；在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【结束计算】
# 计算器类
class TestCalculator:

    def setup_class(self):
        self.c = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    # 加
    @pytest.mark.parametrize('a,b, exc', [
        (1, 2, 3),
        (2, 4, 5),
        (4, 7, 11)
    ])
    def test_add(self, a, b, exc):
        result = self.c.add(a, b)
        assert result == exc

    # 减
    @pytest.mark.parametrize('a,b, exc', [
        (1, 2, 3),
        (2, 4, 5),
        (4, 7, 11)
    ])
    def minus(self, a, b, exc):
        result = self.c.minus(a, b)
        assert result == exc

    # 乘
    @pytest.mark.parametrize('a,b, exc', [
        (1, 2, 3),
        (2, 4, 5),
        (4, 7, 11)
    ])
    def multiple(self, a, b, exc):
        result = self.c.divide(a, b)
        assert result == exc

    # 除
    @pytest.mark.parametrize('a,b, exc', [
        (1, 2, 3),
        (2, 4, 5),
        (4, 7, 11)
    ])
    def divide(self, a, b, exc):
        if b != 0:
            result = self.c.multiple(a, b)
            assert result == exc
        else:
            print("除数不能为0")


