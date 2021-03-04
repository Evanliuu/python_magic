"""
mock测试就是在测试过程中，对于某些不容易构造或者不容易获取的对象，用一个虚拟的对象来创建以便测试的测试方法

1. 解决依赖问题：当我们测试一个接口或者功能模块的时候，如果这个接口或者功能模块依赖其他接口或其他模块，
那么如果所依赖的接口或功能模块未开发完毕，那么我们就可以使用mock模拟被依赖接口，完成目标接口的测试

2. 单元测试：如果某个功能未开发完成，我们又要进行测试用例的代码编写，我们也可以先模拟这个功能进行测试

3. 模拟复杂业务的接口：实际工作中如果我们在测试一个接口功能时，如果这个接口依赖一个非常复杂的接口业务，
那么我们完全可以使用mock来模拟这个复杂的业务接口

4. 前后端联调：如果你是一个前端页面开发，现在需要开发一个功能：根据后台返回的状态展示不同的页面，
那么你就需要调用后台的接口，但是后台接口还未开发完成，是不是你就停止这部分工作呢？
答案是否定的，你完全可以借助mock来模拟后台这个接口返回你想要的数据
"""
from unittest import mock


def add_func(a, b):
    return a + b


# 使用patch装饰器mock函数：第一个参数必须包含父级路径

# 使用return_value返回固定的值
@mock.patch('mock_example.add_func', return_value=10)
def test_1(test):
    print(test(1, 2))  # 10


# 使用side_effect返回多个不同的值，根据执行次数改变，如果执行次数超过给定值上限会抛出异常
@mock.patch('mock_example.add_func', side_effect=[10, 20])
def test_2(test):
    print(test(1, 2))  # 10
    print(test(1, 2))  # 20


# 使用object装饰器mock类
class MockTest(object):
    def test_mock(self):
        pass


# 使用object方法：第一个参数为类名，第二个参数为方法名
@mock.patch.object(MockTest, 'test_mock')
def test_3(test):
    test.return_value = 66
    print(test())  # 66
