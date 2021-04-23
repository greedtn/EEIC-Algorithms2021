# 最大ヒープを実装する
class MyHeap:
    def __init__(self, size):
        self.inf = -10 ** 9
        self.size = size + 1
        self.array = [self.inf] * self.size
        self.last = 0
    
    def add(self, value: int):
        self.last += 1
        self.array[self.last] = value
        return self.check_after_add(self.last)
    
    def remove(self):
        removed = self.array[1]
        self.array[1] = self.array[self.last]
        self.array[self.last] = self.inf
        self.last -= 1
        self.check_after_remove(1)
        print(removed)
    
    def check_after_add(self, i):
        print(i)
        if i < 2:
            return 
        if self.array[i // 2] < self.array[i]:
            self.array[i // 2], self.array[i] = self.array[i], self.array[i // 2]
            return self.check_after_add(i // 2)
        
    def check_after_remove(self, i):
        if 2*i > self.last:
            return
        if self.array[2*i] <= self.array[2*i+1]:
            if self.array[i] < self.array[2*i+1]:
                self.array[i], self.array[2*i+1] = self.array[2*i+1], self.array[i]
                return self.check_after_remove(2*i+1)
        else:
            if self.array[i] < self.array[2*i]:
                self.array[i], self.array[2*i] = self.array[2*i], self.array[i]
                return self.check_after_remove(2*i)

heap = MyHeap(100000)
Q = int(input())
for _ in range(Q):
    x = input()
    if x == "2":
        heap.remove()
    else:
        heap.add(int(x.split()[1]))
        print(heap.array[:6])
        