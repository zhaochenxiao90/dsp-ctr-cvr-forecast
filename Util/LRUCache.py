#!coding:utf8

import collections


# 基于OrderedDict实现
class LRUCache(collections.OrderedDict):
    """
       function:利用collection.OrderedDict数据类型实现最近最少使用算法
                OrderedDict有个特殊方法popitem(Last=False)时则实现队列，弹出最先插入的元素，
                而当Last=True则实现堆栈方法，弹出的是最近插入的那个元素
                实现了两个方法：get(key）取出键中对应的值，若没有返回None
                                set(key, value) 根据LRU特性添加元素
    """

    def __init__(self, size=5):
        self.size = size

    def set(self, key, default=None):
        if key in self:
            self.pop(key)
        if self.size == self.__len__():
            self.popitem(last=False)
        self[key] = default
        return default
    def has_key(self,key):
        if key in self:
            return True
        else:
            return False


if __name__ == '__main__':
    test = LRUCache(3)
    test.set('a', 1)
    test.set('b', 2)
    test.set('c', 3)
    test.set('d', 4)
    test.set('e', 5)
    test.set('f', 6)
    for key, values in test.items():
        print(key, values)
