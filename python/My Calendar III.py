
class MyCalendarThree:

    def __init__(self):
        self.books = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        from bisect import insort_right, insort_left
        insort_right(self.books, [start, 1])
        insort_left(self.books, [end, -1])

        res = 0
        temp = 0
        for a, e in self.books:
            temp += e
            if temp > res:
                res = temp
        return res


        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

# 因为数据范围是 The number of calls to MyCalendarThree.book per test case will be at most 400
# 所以我们不用担心复杂度的问题，不需要什么 fansy 的数据结构。