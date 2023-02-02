'''A Python decorator is a function that takes in a function and  returns it by
adding some functionality
'''


def iam_decorator(func):
    def add_some_functionality():
        '''This function will add some functionality to the decorated
        function'''
        print('[INFO] I was decorated.')
        func()
    return add_some_functionality


@iam_decorator
def i_will_be_decorated():
    '''Basically, a decorated function will be passed to a decorator function
    as a parameter'''
    print('[INFO] I am typical.')


def iam_decorator_with_parameters(func):
    '''This is a decorator with the ability to accept parameters'''
    def add_some_functionality(*args, **kwargs):
        print('*' * 15)
        func(*args, **kwargs)
        print('*' * 15)
    return add_some_functionality


def iam_decorator_with_parameters_1(func):
    def add_some_functionality(*args, **kwargs):
        print('%' * 15)
        func(*args, **kwargs)
        print('%' * 15)
    return add_some_functionality


@iam_decorator_with_parameters
@iam_decorator_with_parameters_1
def i_will_be_decorated_1(msg):
    print(msg)


if __name__ == '__main__':
    # call the to be decorated function
    i_will_be_decorated_1('Hello K.L.!')
