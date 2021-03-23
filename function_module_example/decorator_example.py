# -*- coding:utf-8 -*-
import functools


# 二层装饰器
def decorator(func):  # 执行函数
    def wrapper(*args, **kwargs):  # 函数的实参
        result = dict()
        result['from_func_parameter'] = [args or kwargs]
        result['from_func_return_value'] = func(*args, **kwargs)
        return result
    return wrapper


# 三层装饰器
def full_decorator(value=None):  # 装饰器的实参
    def decorator(func):  # 执行函数
        def wrapper(*args, **kwargs):  # 函数的实参
            result = dict()
            result['from_func_parameter'] = [args or kwargs]
            result['from_func_return_value'] = func(*args, **kwargs)
            result['from_decorator_parameter'] = value
            return result
        return wrapper
    return decorator


# 使用wraps
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


@decorator
def example1(*args):
    return 'hi {}'.format(args)


@full_decorator('Hello World!')
def example2(*args):
    return 'hi {}'.format(args)


if __name__ == '__main__':
    print('使用wraps结果：')
    print('name: {}'.format(example.__name__))
    print('docstring: {}'.format(example.__doc__))

    print('二层装饰器结果：')
    print(example1('example1'))

    print('三层装饰器结果：')
    print(example2('example2'))
