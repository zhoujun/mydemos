#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


class Foo:
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print 'class decorator runing'
        self._func()
        print 'class decorator ending'

@Foo
def bar():
    print 'bar'


def log(text=''):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print 'before function %s' % text
            ret = function(*args, **kwargs)
            print 'after function %s' % text
            return ret
        return wrapper
    return decorator

@log('log text')
def func():
    print 'func() run.'

# def log(function):
#     def wrapper(*args, **kwargs):
#         print 'before function'
#         function(*args, **kwargs)
#         print 'after function'

#     return wrapper

# @log
# def func():
#     print 'func() run.'

if __name__ == '__main__':
    bar()
    func()
    print func.__name__
