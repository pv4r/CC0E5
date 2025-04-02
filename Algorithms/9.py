# Define an abstract data type (ADT) that combines the characteristics of a stack and a queue,
# commonly known as a deque (double-ended queue).

# Linked list Implementation of Deque
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Only one pointer to the next node

class Deque:
    def __init__(self):
        self.head = None  # Only one reference to the first node

    def is_empty(self):
        return self.head is None

    def push_front(self, item):  
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, item):  
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:  # To the last node
                current = current.next
            current.next = new_node  # Add the new node at the end

    def pop_front(self):  
        if self.is_empty():
            raise IndexError("Deque is empty")
        removed_item = self.head.data
        self.head = self.head.next  # Move the head to the next node
        return removed_item

    def pop_back(self):  
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.head.next is None:  # Only one element
            removed_item = self.head.data
            self.head = None
            return removed_item

        current = self.head
        while current.next.next:  # Find the penultimate node
            current = current.next
        removed_item = current.next.data
        current.next = None  # Delete the last node
        return removed_item

    def front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.head.data

    def back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        current = self.head
        while current.next:  # To the last node
            current = current.next
        return current.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Circular Array Implementation of Deque

class CircularDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front # Because the modular arithmetic

    def push_front(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity # Because the modular arithmetic
        self.queue[self.front] = item

    def push_back(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity # Because the modular arithmetic
        self.queue[self.rear] = item

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        removed_item = self.queue[self.front]
        if self.front == self.rear:  # Only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed_item

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        removed_item = self.queue[self.rear]
        if self.front == self.rear:  # Only one element
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.capacity # Because the modular arithmetic
        return removed_item

    def front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.queue[self.front]

    def back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.queue[self.rear]

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity # Because the modular arithmetic
        print()

