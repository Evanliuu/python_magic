def func(value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = list()
            # 添加调用函数的实参
            result.append(*args, **kwargs)
            # 添加调用函数的返回值
            result.append(func(*args, **kwargs))
            # 添加装饰器的实参
            result.append(value)
            return result
        return wrapper
    return decorator


@func('Hello World!')
def function(*args):
    return 'hi {}'.format(args)


if __name__ == '__main__':
    print(function('Evan'))
