#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Foo:

    def __init__(self):
        pass

    def func(self):
        print 'func'

    @classmethod
    def class_func(cls):
        print 'class func'

    @staticmethod
    def static_func():
        print 'static func'


f = Foo()
f.func()


Foo.class_func()
Foo.static_func()
