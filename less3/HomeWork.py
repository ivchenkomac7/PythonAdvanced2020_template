# Создать класс структуры данных Стек, Очередь. Создать класс
# комплексного числа и реализовать для него арифметические
# операции.

from collections import deque


class Stack(deque):
    def push(self, x):
        super().append(x)

    def pop(self):
        return super().pop()


class Queue(deque):
    def enqueue(self, x):
        self.append(x)

    def dequeue(self):
        return self.popleft()


s = Stack()
q = Queue()

s.push(1)
s.push(2)
s.push(4)

q.enqueue(1)
q.enqueue(3)
q.enqueue(9)

print(s)
print(q)

s.pop()
q.dequeue()

print(s)
print(q)

class Complex:
    pass
