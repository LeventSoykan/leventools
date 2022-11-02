import pandas
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = pandas.Timestamp('today')
        val = func(*args, **kwargs)
        end = pandas.Timestamp('today')
        delta = end - start
        print(f'Process took: {delta.components.minutes} min, {delta.components.seconds},'
              f'secs {delta.components.milliseconds} ms')
        return val
    return wrapper


def return_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if not val:
            print(f'Process does not return any value - {type(val)}')
        elif len([val]) > 1:
            print([type(n) for n in val])
        else:
            print(type(val))
        # print(val)
        return val
    return wrapper


if __name__ == '__main__':

    # @timer
    # def wait(name):
    #     time.sleep(1.5)
    #     print(f'Hello {name}')
    #
    # wait('Levent')
    #
    # @return_type
    # def return_func(num1, num2):
    #     return num1*30
    #
    # print(return_func(1, 3))

    # @run_n_times(3)
    # def greet(name):
    #     print(f'Hello {name}')
    #
    # greet('Levent')
