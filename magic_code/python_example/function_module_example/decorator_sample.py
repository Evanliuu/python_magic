def func(value=None):
    def decorator(expect):
        def wrapper(*args, **kwargs):
            result = []
            # user use of value
            result.append(*args, **kwargs)
            # from function return
            result.append(expect(*args, **kwargs))
            result.append(value)
            return result
        return wrapper
    return decorator


@func('Hello World')
def function(*args):
    return 'hi {}'.format(args)


if __name__ == '__main__':
    print(function('Evan'))
