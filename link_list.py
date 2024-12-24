#在python中可以使用collections的deque模块
from collections import deque
#创建链表

linkedlist = deque()

#添加元素
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
print(linkedlist)

#插入
linkedlist.insert(2,99)
print(linkedlist)