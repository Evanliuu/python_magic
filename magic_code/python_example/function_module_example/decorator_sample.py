# 二层装饰器
def decorator(func):  # 执行函数
    def wrapper(*args, **kwargs):  # 函数的实参
        result = dict()
        result['from_func_parameter'] = [args or kwargs]
        result['from_func_return_value'] = func(*args, **kwargs)
        return result
    return wrapper


# 三层装饰器
def three_tool(value=None):  # 装饰器的实参
    def decorator(func):  # 执行函数
        def wrapper(*args, **kwargs):  # 函数的实参
            result = dict()
            result['from_func_parameter'] = [args or kwargs]
            result['from_func_return_value'] = func(*args, **kwargs)
            result['from_decorator_parameter'] = value
            return result
        return wrapper
    return decorator


@decorator
def example1(*args):
    return 'hi {}'.format(args)


@three_tool('Hello World!')
def example2(*args):
    return 'hi {}'.format(args)


if __name__ == '__main__':
    print('二层装饰器结果：')
    print(example1('Evan1'))
    print('三层装饰器结果：')
    print(example2('Evan2'))
