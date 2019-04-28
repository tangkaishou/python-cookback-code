"""
利用heapq模块
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0   # 作用是确保两个相同权重的节点保持插入时的顺序的相反顺序弹出

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'),1)
    q.push(Item('bar'),5)
    q.push(Item('spam'),4)
    q.push(Item('grok'),1)

    print(q._queue)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

