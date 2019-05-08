"""
heapq模块的学习
heapq模块详解

heapq.heappush(heap, item) 把item添加到heap中（heap是一个列表）

heapq.heappop(heap) 把堆顶元素弹出，返回的就是堆顶

heapq.heappushpop(heap, item) 先把item加入到堆中，然后再pop，比heappush()再heappop()要快得多

heapq.heapreplace(heap, item) 先pop，然后再把item加入到堆中，比heappop()再heappush()要快得多

heapq.heapify(x) 将列表x进行堆调整，默认的是小顶堆

heapq.merge(*iterables) 将多个列表合并，并进行堆调整，返回的是合并后的列表的迭代器

heapq.nlargest(n, iterable, key=None) 返回最大的n个元素（Top-K问题）

heapq.nsmallest(n, iterable, key=None) 返回最小的n个元素（Top-K问题）

"""

import heapq


li = [1,6,3,2,5,7,9]

heapq.heapify(li)


for i in range(len(li)):
    print(heapq.heappop(li))

