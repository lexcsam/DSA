#https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    def enqueue(self, x):
        self.enqueue_stack.append(x)
    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
    def front(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack[-1]
q = int(input())
queue = Queue()
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        queue.enqueue(int(query[1]))
    elif query[0] == "2":
        queue.dequeue()
    elif query[0] == "3":
        front_element = queue.front()
        print(front_element)
