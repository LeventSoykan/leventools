

def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


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
