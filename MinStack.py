class MinStack:
    # @param x, an integer
    # @return an integer
    # https://leetcode.com/discuss/15687/oj-bug-in-python
    def __init__(self):
        self.l = []
    def push(self, x):
        if not self.l:
            self.m = x
        self.l += [x-self.m] # then we know the last min
        if x - self.m < 0:
            self.m = x

    # @return nothing
    def pop(self):
        if not self.l:
            return None
        t = self.l.pop()
        if t < 0:
            self.m = self.m - t
            

    # @return an integer
    def top(self):
        if not self.l :
            return None
        temp = self.l[-1] # can just use -1
        if temp < 0: # different conditions
            return self.m
        return self.m + temp
        

    # @return an integer
    def getMin(self):
        return self.m

s = MinStack() 
s.push(2147483646)
s.push(2147483646)
s.push(2147483647)
print(s.l, s.m, s.top())
s.pop()
print(s.l, s.m, s.getMin())
s.pop()
print(s.l, s.m, s.getMin())
s.pop()
print()
s.push(2147483647)
print(s.l, s.m, s.top())
print(s.l, s.m, s.getMin())
s.push(-2147483648)
print(s.l, s.m, s.top())
print(s.l, s.m, s.getMin())
s.pop()
print(s.l, s.m, s.getMin())
