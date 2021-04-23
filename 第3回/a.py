Q, K = map(int, input().split())

class Queue:
    def __init__(self, size: int):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size
    
    def next_def(self, a: int):
        return (a + 1) % self.size

    def enqueue(self, a: int):
        if self.head == self.next_def(self.tail):
            print("queue is full")
        else:
            self.queue[self.tail] = a
            self.tail = self.next_def(self.tail)
            # print(self.queue)
    
    def dequeue(self):
        if self.head == self.tail:
            print("queue is empty")
        else:
            tmp = self.queue[self.head]
            self.queue[self.head] = None
            self.head = self.next_def(self.head)
            print(tmp)

q = Queue(K+1)
for i in range(Q):
    x = input()
    if x == "2":
        q.dequeue()
    else:
        q.enqueue(int(x.split()[1]))
