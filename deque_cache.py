class Deque:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError('capacity must be an integer greater than 0')
        self.capacity = capacity
        self.items = []
    #проверка на полноту
    def is_full(self):
        return len(self.items) == self.capacity
    #проверка на пустоту
    def is_empty(self):
        return len(self.items) == 0
    #посмотреть размер
    def size(self):
        return len(self.items)
    #добавить в конец и вытащить вначале
    def push_back(self, value):
        if self.is_full():
            self.items.pop(0)
        self.items.append(value)
    #вытащить вконце и добавить вначало
    def push_front(self, value):
        if self.is_full():
            self.items.pop()
        self.items.insert(0, value)
    #вытищить первый элемент
    def pop_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.items.pop(0)
    #вытащить последний элемент
    def pop_back(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.items.pop()
    #посмотреть первый
    def peek_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.items[0]
    #посмотреть последний
    def peek_back(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.items[-1]
class Cache:
    def __init__(self, capacity):
        self.buffer = Deque(capacity)
        self.hits = 0
        self.misses = 0
    def request(self, value):
        if x in self.buffer.items:
            self.hits += 1
            return True
        else:
            self.misses += 1
            self.buffer.push_back(value)
            return False
def test(name, func):
    try:
        result = func()
        print(name, "-", result)
    except Exception as e:
        print(name, "- Error:", type(e).__name__, "-", e)
# Набор 1: переполнение через push_back
d = Deque(3)
for x in [1, 2, 3, 4]:
    d.push_back(x)
print("Набор 1:", d.items)
# Набор 2: переполнение через push_front
d = Deque(3)
for x in [1, 2, 3]:
    d.push_back(x)
d.push_front(0)
print("Набор 2:", d.items)
# Набор 3: пустой дек
d = Deque(3)
test("Набор 3, pop_front", d.pop_front)
test("Набор 3, peek_back", d.peek_back)
# Набор 4: некорректный размер
test("Набор 4, размер 0", lambda: Deque(0))
test("Набор 4, размер -5", lambda: Deque(-5))
test("Набор 4, размер 'abc'", lambda: Deque("abc"))
# Набор 5: кэш
c = Cache(3)
for x in [1, 2, 3, 1, 4, 2, 5]:
    c.request(x)
print("Набор 5:", c.buffer.items, "hits =", c.hits, "misses =", c.misses)