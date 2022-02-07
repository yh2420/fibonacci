from fibonacci import fib


def test_fibonacci():
    for n, v in enumerate([0, 1, 1, 2, 3, 5]):
        assert fib(n) == v # assert 表达式为真，则继续执行，但如果为假，则发生错误
