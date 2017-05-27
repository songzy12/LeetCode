class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        if sum(machines) % len(machines):
            return -1
        avg = sum(machines) / len(machines)
        machines = map(lambda x: x-avg, machines)
        print machines
        ans = total = 0       
        # if target > 0, then it can only move to one another slot
        # if target < 0, then it can receive from two slots 
        for target in machines:
            total += target
            ans = max([ans, target, abs(total)])
        return ans

if __name__ == '__main__':
    machines = [0,0,11,5]
    print Solution().findMinMoves(machines)
