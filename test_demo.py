import pytest


class TestDemo:

    # 'a,b' == ['a','b'] == ('a','b')
    # 这种参数化时值为list类型，若是dict类型则只取字典中的key
    @pytest.mark.parametrize('a,b', [
        (10, 20),
        (10, 10),
        ('a', 'a1')
    ])
    def test_a(self, a, b):
        assert a == b

    @pytest.mark.parametrize('a', [1, 2])
    @pytest.mark.parametrize('b', [3, 4])
    def test_b(self, a, b):
        print('a == %s, b == %s' % (a, b))


if __name__ == "__main__":
    pytest.main(["-s", "test_demo.py"])
