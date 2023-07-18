import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-ex', '--example', type=str, help='Choose an example to\
run')
args = vars(parser.parse_args())


def addition(*args):
    '''
    *args allow a function to take any number of positional arguments
    '''
    result = 0
    for i in args:
        result += i
    return result


def addition_1(a, b, *args, option=True):
    result = 0
    if option:
        for i in args:
            result += i
        return a + b + result
    else:
        return result


def arg_printer(a, b, *args):
    '''
    *args can be used with named variables
    '''
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'args: {args}')


def arg_printer_1(a, b, option=True, **kwargs):
    '''
    **kwargs allow a function to take any number of keyword arguments
    '''
    print(a, b)
    print(option)
    print(kwargs)


def arg_printer_2(a, b, *args, option=True, **kwargs):
    print(a, b)
    print(args)
    print(option)
    print(kwargs)


def arg_printer_3(*args):
    print(args)


def arg_printer_4(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    if args['example'] == '1':
        print('[INFO] Example 1')
        print(f"Result with three positional arguments {addition(3, 4, 5)}")
        print(f"Result with four positional arguments {addition(3, 4, 5, 6)}")

    elif args['example'] == '2':
        print('[INFO] Example 2')
        print(arg_printer(3, 4, 5, 8, 3))

    elif args['example'] == '3':
        print('[INFO] Example 3')
        print('[INFO] Key word arguments are always after the positional' +
              'arguments')

    elif args['example'] == '4':
        print('[INFO] Example 4')
        print(f'Result with option equals True: {addition_1(10, 11, 12)}')
        print(f'Result with option equals False: {addition_1(10, 11, 12, option=False)}')

    elif args['example'] == '5':
        print('[INFO] Example 5')
        print(arg_printer_1(4, 5, option=False, param1=2, param2=1))

    elif args['example'] == '6':
        print('[INFO] Example 6')
        print(arg_printer_2(5, 6, 7, 8, 9, 10, param1=2, param2=5))

    elif args['example'] == '7':
        print('[INFO] Example 7')
        print('[INFO] Packing and unpacking variables using *args')
        # it is like passing 1 variable to the function
        print(f'Passing a list without unpacking: {arg_printer_3([1, 2, 4])}')
        # it is like passing more than 1 variable to the function
        print(f'Passing an unpacked list: {arg_printer_3(*[1, 2, 4])}')

    else:
        print('[INFO] Example 8')
        print('[INFO] Packing and unpacking variables using **kwargs')
        try:
            print(f"Passing a dictionary without unpacking: {arg_printer_4({'guava': 20, 'orange': 10})}")
        except TypeError:
            print('\033[93;1m[WARNING] The function expects key word arguments, but we passed in a positional argumet, hence the TypeError being raised!\033[0m')
        print(f"Passing an unpacked dictionary: {arg_printer_4(**{'guava': 20, 'orange': 10})}")
