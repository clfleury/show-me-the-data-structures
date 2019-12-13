class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

    def set_next(self, node):
        self.next = Node(node)

    def set_previous(self, node):
        self.previous = Node(node)

    def set_value(self, value):
        self.value = value

    def get_previous(self):
        return self.previous

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        self.tail.next = Node(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next


class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = LinkedList()
        self.dict = {}

    def test_data_integrity(self):
        node = self.list.tail
        while node:
            node = node.previous

    def get(self, key):

        if key in self.dict:
            if self.dict[key].get_previous() and self.dict[key].get_next():
                self.dict[key].get_previous().next = self.dict[key].get_next()
                self.dict[key].get_next().previous = self.dict[key].get_previous()
            elif self.dict[key].get_next():
                self.list.head.next.previous = None
                self.list.head = self.list.head.next
                self.list.tail.next = self.dict[key]
                self.list.tail.next.previous = self.list.tail
                self.list.tail = self.list.tail.next
                self.list.tail.next = None

            return self.dict[key].value

        return -1

    def set(self, key, value):
        self.list.append(value) #set as most recently used item
        self.dict[key] = self.list.tail

        if len(self.dict) > self.capacity:
            del self.dict[key]
            self.list.head = self.list.head.get_next() #reduce list length if capacity is reached

#Example1
our_cache = Cache(4)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

#our_cache.test_data_integrity()

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached its capacity and 3 was the least recently used entry

our_cache.test_data_integrity()

#Example2 -edge case
our_cache_2 = Cache(0)

our_cache_2.set(21, 21)
our_cache_2.set(31, 31)
our_cache_2.set(8, 8)
our_cache_2.set(322, 322)
our_cache_2.set(321, 321)

print(our_cache_2.get(321))  # returns -1
print(our_cache_2.get(322))  # returns -1
print(our_cache_2.get(21))  # returns -1
print(our_cache_2.get(3))     # returns -1

#Example3 -edge case
our_cache_3 = Cache(-1)

our_cache_3.set(40, 40)

print(our_cache_3.get(40)) #returns -1 because the size of the cache can't take values

#Example 4
our_cache_4 = Cache(2)
our_cache_4.set(1, 1)
our_cache_4.set(2, 2)
our_cache_4.set(1, 10)
print(our_cache_4.get(1))
# should return 10
print(our_cache_4.get(2))
# should return 2

