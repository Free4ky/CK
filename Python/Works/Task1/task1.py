from functools import reduce


def my_add(*args):
    try:
        return reduce(lambda x, y: x + y, args)
    except (ValueError, TypeError):
        return 'Error'


def my_sub(*args):
    try:
        return reduce(lambda x, y: x - y, args)
    except (ValueError, TypeError):
        return 'Error'


def my_mul(*args):
    try:
        return reduce(lambda x, y: x * y, args)
    except (ValueError, TypeError):
        return 'Error'


def my_div(*args):
    try:
        return reduce(lambda x, y: x / y, args)
    except (ValueError, TypeError):
        return 'Error'


def my_mod(a, b):
    try:
        return a % b
    except (ValueError, TypeError):
        return 'Error'


def my_sqrt(x, power=2):
    try:
        return x ** (1 / power)
    except (ValueError, TypeError):
        return 'Error'
