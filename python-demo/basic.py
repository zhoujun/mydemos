#!/usr/bin/env python
#-*- coding: utf-8 -*-

a_list = [1, 2, 4, 7, 9, 3, 5, 6]

# 遍历列表
# for i, a in enumerate(a_list):
#     print i, a

# for i in range(0, len(a_list)):
#     print a_list[i]

# for i in xrange(0, len(a_list)):
#     print i, a_list(i)

# for i in xrange(len(a_list), 0, -1):
#     print i, a_list[i-1]

# 反转列表
# print a_list[::-1]
# a_list.reverse()
# print a_list

# 反转字符串
# s = 'abcdefg'
# print s[::-1]

# 列表推导
# print [x for x in  a_list]

# lambda表达式
# print [(lambda x : x + 2) for x in a_list]

# map
# print map(lambda x: x ** 2, a_list)

# filter
# print filter(lambda x: x > 4, a_list)

# reduce
# print reduce(lambda a, b : a + b, a_list)
# print sum(a_list)

########################################################

# 字典
a_dict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g'
}

# for k, v in a_dict.iteritems():
#     print k, v

# print a_dict.keys(), a_dict.values()



# 按照key排序
# print sorted(a_dict.items(), key=lambda d: d[0])
# 按照value排序
# print sorted(a_dict.items(), key=lambda d: d[1])

# # 字典的浅拷贝
# dict1 = {"a" : "apple", "b" : "grape"}
# dict2 = {"c" : "orange", "d" : "banana"}
# dict2 = dict1.copy()
# print dict2

#字典的深拷贝
# import copy

# dict1 = {"a" : "apple", "b" : {"g" : "grape","o" : "orange"}}
# dict2 = copy.deepcopy(dict1)

# dict2["b"]["g"] = "orange"
# print 'deep', dict1, dict2

# dict3 = copy.copy(dict1)
# dict3["b"]["g"] = "orange"
# print 'copy', dict1, dict2

# k = ['a', 'b', 'c']
# v = [1, 2, 3]
# print dict(zip(k, v))

# d = { c:ord(c) for c in 'abc' }
# print d

########################################################
# 装饰器
# def hello(func):
#     def wrapper():
#         print 'hello'
#         func()
#     return wrapper

# @hello
# def a():
#     print 'world'

# a()

# def deco(func):
#     def wrapper(a, b):
#         return func(a, b)
#     return wrapper

# @deco
# def test(a, b):
#     return a + b

# print test(1, 2)

# 单例装饰器
# def singleton(cls):
#     instances = dict()  # 初始为空
#     def _singleton(*args, **kwargs):
#         if cls not in instances:  #如果不存在, 则创建并放入字典
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return _singleton

# class Test(object):
#     pass

# t1 = Test()
# t2 = Test()
# # 两者具有相同的地址
# print t1, t2

# l = [{'name': 'name', 'age': 10}]
# for name, age in map(lambda x: (x['name'], x['age']), l):
#     print(name, age)


# a = [1,2,3,4,5,6,7,8]
# print map(lambda x : x + 1, a)

# lambda x, y: x * 10 + y
# def fn(x, y):
#     print x, y
#     return x * 10 + y

# print reduce(fn, [1, 3, 5, 7, 9])

# yield 是一个关键字，类似于return，不同之处在于，yield返回的是一个生成器
def createGenerator():
    myList = [1,2,3,4]
    for i in myList:
        yield i * i

myGenerator = createGenerator()
print(myGenerator)

for i in myGenerator:
    print i





































