class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def convert(timePoint):
            return sum([60**(1-i)*n for i, n in enumerate(map(int, timePoint.split(":")))])

        timePoints = sorted(map(convert, timePoints))
        ans = 24*60
        for i in range(len(timePoints)-1):
            ans = min(ans, timePoints[i+1]-timePoints[i]
                      )
        ans = min(ans, timePoints[0]+24*60-timePoints[-1])
        return ans
            
if __name__ == '__main__':
    timePoints = ["23:59","00:00"]
    print Solution().findMinDifference(timePoints)
