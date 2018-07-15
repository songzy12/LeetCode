class Solution(object):

    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        cnt = 0
        available = []
        distance = startFuel
        i = 0
        while distance < target:
            while i < len(stations) and stations[i][0] <= distance:
                heappush(available, -stations[i][1])
                i += 1
            if not available:
                return -1
            temp = -heappop(available)
            distance += temp
            cnt += 1
        return cnt


target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
print Solution().minRefuelStops(target, startFuel, stations)
