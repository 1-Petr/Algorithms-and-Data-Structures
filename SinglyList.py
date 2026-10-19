class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def push_back(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
    def push_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.count += 1
    def pop_front(self):
        if self.head is None:
            return False
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return True
    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.data == value:
                return "нашли"
            cur = cur.next
        else:
            return "не нашли"

    def binary_search(a, key):
        l = 0
        r = len(a) - 1
        while l <= r:
            m = (l + r) // 2
            if a[m] == key:
                return m
            if a[m] < key:
                l = m + 1
            else:
                r = m - 1
        return -1
#тест
L = SinglyList()
L.push_back(5)
L.push_back(6)
L.push_back(7)
print(L.head.data, L.tail.data, L.count, L.find(3))

L.push_front(4)
print(L.head.data, L.tail.data, L.count, L.find(6))

L.pop_front()
print(L.head.data, L.tail.data, L.count)

print(L.find(6))
print(L.find(99))

L.pop_front()
L.pop_front()
L.pop_front()
print(L.head, L.tail, L.count)
print(L.pop_front())