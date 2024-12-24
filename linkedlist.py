class Node:
    def __init__(self, data=None):
        self.data = data  # 节点的数据部分
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None  # 链表的头指针，初始化为空链表

    # 插入到链表的末尾
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # 如果链表为空，直接将新节点设为头节点
        else:
            last_node = self.head
            while last_node.next:  # 找到链表的最后一个节点
                last_node = last_node.next
            last_node.next = new_node  # 将新节点插入到最后一个节点的后面

    # 插入到链表的头部
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # 新节点指向当前的头节点
        self.head = new_node  # 将新节点设为头节点

    # 在指定位置插入节点（位置从 0 开始）
    def insert(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        current = self.head
        index = 0
        while current and index < position - 1:  # 遍历到目标位置的前一个节点
            current = current.next
            index += 1
        if not current:  # 如果指定位置超出链表长度
            print("Position out of bounds")
            return
        new_node.next = current.next  # 新节点的 next 指向当前节点的 next
        current.next = new_node  # 当前节点的 next 指向新节点

    # 删除指定位置的节点
    def delete(self, position):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        if position == 0:  # 删除头节点
            self.head = current.next
            current = None
            return
        index = 0
        prev = None
        while current and index < position:
            prev = current
            current = current.next
            index += 1
        if current is None:  # 如果指定位置超出链表长度
            print("Position out of bounds")
            return
        prev.next = current.next  # 将前一个节点的 next 指向当前节点的 next
        current = None  # 删除节点

    # 打印链表的内容
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 查找链表中的节点
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # 获取链表的长度
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 反转链表
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


l1 = LinkedList()
l1.append(1)
l1.append(20)
l1.display()


