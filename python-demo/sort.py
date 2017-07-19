#!/usr/bin/env python
#-*- coding: utf-8 -*-

# http://javayhu.me/blog/2014/05/07/python-data-structures---c2-sort/

def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                # temp = a_list[i]
                # a_list[i] = a_list[i + 1]
                # a_list[i + 1] = temp
                a_list[i],a_list[i+1] = a_list[i+1], a_list[i]
        pass_num = pass_num - 1

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        # temp = a_list[fill_slot]
        # a_list[fill_slot] = a_list[pos_of_max]
        # a_list[pos_of_max] = temp
        a_list[fill_slot],a_list[pos_of_max]=a_list[pos_of_max],a_list[fill_slot]

def selection_sort2(list_):
    count = len(list_)
    for i in range(0, count:
        min_pos = i
        for j in range(i + 1, count):
            if (list_[min_pos] > list_[j]):
                min_pos = j
            list_[min_pos], list_[i] = list_[i], list_[min_pos]
    return list_

def insertion_sort(a_list):
    for index in range(1, len(a_list)): #[2, 4, 3, 7, 1, 9]
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

def insertion_sort_binarysearch(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low=0
        high=index-1
        while low<=high:
            mid=(low+high)/2
            if a_list[mid]>current_value:
                high=mid-1
            else:
                low=mid+1
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position -1
        a_list[position] = current_value

def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0;j=0;k=0;
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j=j+1
            k=k+1
    print("Merging ", a_list)

def quick_sort(seq): # [7, 3, 1, 4, 6, 9, 8, 2, 11, 18]
    if len(seq) <= 0:
        return []
    else:
        center = seq[0] # 7
        lesser = quick_sort([x for x in seq[1:] if x < center])     # [3, 1, 4, 6, 2]
        greater = quick_sort([ x for x in seq[1:] if x >= center])  # [9, 8, 11, 18]
        return lesser + [center] + greater

def test_quick_sort():
    a_list=[20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    print quick_sort(a_list)

def test_bubble_sort():
    # 1, bubble sort
    a_list=[20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    short_bubble_sort(a_list)
    print(a_list)

def test_selection_sort():
    # 2, selection sort
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(a_list)
    print(a_list)

def test_insertion_sort():
    # 3, insertion sort
    a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
    insertion_sort(a_list)
    print(a_list)

    insertion_sort_binarysearch(a_list)
    print(a_list)

def test_merge_sort():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(a_list)
    print(a_list)


fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

def fib_(n):
    if n <= 2:
        return n
    else:
        return fib_(n-1) + fib_(n-2)

def fib2(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b

def binary_search(l, t):
    low, high = 0, len(l) - 1
    while low < high:
        print low, high
        mid = (low + high) / 2
        print mid
        if l[mid] > t:
            high = mid
        elif l[mid] < t:
            low = mid + 1
        else:
            return mid
    return low if l[low] == t else False

def bubble_sort(list_):
    for i in xrange(0, list_[len(list_-1)]):
        a, b = list_[i], list[i+1]
        if (a > b):
            list_[i], list_[i+1] = b, a
    return list_

# 合并两个有序列表
def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)

def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])

def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp

def quicksort(array):
    less, greater = [], []
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()
        for x in array:
            if x <= pivot: less.append(x)
            else: greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)

def quicksort2(list_):
    if (len(list_) <= 0):
        return list_
    else:
        left, right = [], []
        flag = list_[0]
        left = quicksort2([x for x in list_[1:] if x < flag])
        right = quicksort2([x for x in list_[1:] if x >= flag])
        return left + [flag] + right

def binary_search(list_, key):
    low, high = 0, len(list_) - 1
    while(low < high):
        mid = (low + high) / 2
        if (list_[mid] < key): # [2, 3, 4, 5, 7, 8, 9]
            low = mid + 1
        elif (list_[mid] > high):
            high = mid
        else:
            return mid
    return low

def insert_sort(list_):
    for i in xrange(1, len(list_) - 1):
        current = list_[i]
        pos = i
        while (current > 0 and current < list_[i - 1]):
            list_[i] = list_[i - 1]
            pos = pos - 1
        list_[i] = current

def insert_sort2(lists):
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return listss

if __name__ == '__main__':
    # test_quick_sort()
    # print fib(8)

    # list1 = ['b','c','d','b','c','a','a']
    # list2 = list(set(list1))
    # list2.sort(key=list1.index)
    # print list2

    list_ = [2,3,4,5,7,8,9]
    print binary_search(list_, 7)
    # print insert_sort(list_), list_


    # list1 = [1,3,5]
    # list2 = [2,4,6]
    # print loop_merge_sort(list1, list2)
    # print list(set(list1) | set(list2))













