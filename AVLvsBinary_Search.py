class StaticArray:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError('capacity must be an integer greater than 0')
        self.capacity = capacity
        self.items = [0] * capacity
        self.count = 0

    def is_full(self):
        #проверка на полноту
        return self.count == self.capacity

    def find_position(self, key):
        #бинарный поиск: позиция первого элемента >= key, O(log n)
        lo, hi = 0, self.count
        while lo < hi:
            mid = (lo + hi) // 2
            if self.items[mid] < key:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def contains(self, key):
        #поиск O(log n)
        i = self.find_position(key)
        return i < self.count and self.items[i] == key

    def insert(self, key):
        #поиск места O(log n), потом сдвиг вправо O(n)
        if self.is_full():
            raise OverflowError('array is full')
        i = self.find_position(key)
        if i < self.count and self.items[i] == key:
            return False
        self.items[i + 1:self.count + 1] = self.items[i:self.count]
        self.items[i] = key
        self.count += 1
        return True

    def delete(self, key):
        #поиск O(log n), потом сдвиг влево O(n)
        i = self.find_position(key)
        if i < self.count and self.items[i] == key:
            self.items[i:self.count - 1] = self.items[i + 1:self.count]
            self.count -= 1
            return True
        return False
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    #высота узла (None = 0)
    return node.height if node is not None else 0


def update_height(node):
    #пересчитать высоту узла
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def balance_factor(node):
    #разница высот поддеревьев
    return get_height(node.left) - get_height(node.right)


def rotate_right(y):
    #малый правый поворот ll
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x


def rotate_left(x):
    #малый левый поворот rr
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        #вставить ключ
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        #рекурсивная вставка + балансировка
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        update_height(node)
        bf = balance_factor(node)

        if bf > 1:
            if key < node.left.key:
                return rotate_right(node)
            else:
                node.left = rotate_left(node.left)
                return rotate_right(node)

        if bf < -1:
            if key > node.right.key:
                return rotate_left(node)
            else:
                node.right = rotate_right(node.right)
                return rotate_left(node)

        return node

    def delete(self, key):
        #удалить ключ
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        #рекурсивное удаление + балансировка
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = node.right
            while succ.left is not None:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)

        update_height(node)
        bf = balance_factor(node)

        if bf > 1:
            if balance_factor(node.left) >= 0:
                return rotate_right(node)
            else:
                node.left = rotate_left(node.left)
                return rotate_right(node)

        if bf < -1:
            if balance_factor(node.right) <= 0:
                return rotate_left(node)
            else:
                node.right = rotate_right(node.right)
                return rotate_left(node)

        return node

    def contains(self, key):
        #есть ли ключ
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def min(self):
        #минимальный ключ
        if self.root is None:
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def max(self):
        #максимальный ключ
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    def inorder(self):
        #отсортированный список ключей
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        #лево - узел - право
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)

    def size(self):
        #количество узлов
        return self._size(self.root)

    def _size(self, node):
        #рекурсивный подсчёт
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def height(self):
        #высота дерева
        return get_height(self.root)

    def is_valid_bst(self):
        #проверка свойства bst
        return self._is_valid(self.root, float('-inf'), float('inf'))

    def _is_valid(self, node, low, high):
        #проверка с диапазоном
        if node is None:
            return True
        if not (low < node.key < high):
            return False
        return (self._is_valid(node.left, low, node.key) and
                self._is_valid(node.right, node.key, high))

    def is_balanced(self):
        #проверка баланса всех узлов
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        #рекурсивная проверка bf <= 1
        if node is None:
            return True
        if abs(balance_factor(node)) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)
