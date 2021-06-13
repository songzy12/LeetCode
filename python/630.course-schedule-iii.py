class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # do not use dp all the time
        import heapq
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda (t, end): end):
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)

courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print Solution().scheduleCourse(courses)
