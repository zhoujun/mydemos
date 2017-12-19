#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://segmentfault.com/a/1190000002915566
"""
字符串相似度检测
"""
import Levenshtein

"""
Levenshtein.hamming(str1, str2)
计算汉明距离。要求str1和str2必须长度一致。是描述两个等长字串之间对应 位置上不同字符的个数。
"""


def test_distance(s, arr):
    """
    计算编辑距离（也称为 Levenshtein距离）。
    是描述由一个字串转化成另一个字串最少的操作次数，在其中的操作包括插入、删除、替换。
    """
    for x in arr:
        print Levenshtein.distance(s, x)


def test_ratio(s, arr):

    """
    计算莱文斯坦比。计算公式r = (sum - ldist) / sum, 其中sum是指str1 和 str2 字串的长度总和，ldist是 类编辑距离
    注意 ：这里的类编辑距离不是2中所说的编辑距离，2中三种操作中每个操作+1，而在此处，删除、插入依然+1，但是替换+2
    这样设计的目的：
    ratio('a', 'c')，sum=2, 按2中计算为（2-1）/2 = 0.5,’a','c'没有重合，显然不合算，但是替换操作+2，就可以解决这个问题。
    """
    for x in arr:
        print Levenshtein.ratio(s, x)


def test_jaro(s, arr):

    for x in arr:
        print Levenshtein.jaro(s, x)


def test_jarao_winkler(s, arr):
    for x in arr:
        print Levenshtein.jaro_winkler(s, x)


if __name__ == '__main__':
    a = "Chicago"
    b = "Chicago Heights"
    c = "Chicago Ridge"

    arr = [a, b, c]
    s = "Chicago"

    # arr = ['0932443', '0984343', '0943433', '0932643', '093223']
    # s = "0932"

    # arr = [
    #     '1411 New York Ave, Saint Cloud, FL 34769',
    #     '2605 New York St, Melbourne, FL 32904',
    #     '3912 New York Ave, Fair Oaks, CA 95628',
    #     '434 New York Ave, Saint Cloud, FL 34769',
    #     '77010 New York Ave, Palm Desert, CA 92211'
    # ]
    # s = 'Melbourne'
    test_jarao_winkler(s, arr)

