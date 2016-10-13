class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        states = self.getPossibleStates(num, 4 + 6)
        res = []
        for state in states:
            res += self.convert(state)
        return res
        
    def getPossibleStates(self, num, width):
        if num > width:
            return []
        if num == width:
            return ['1' * width]
        if num == 0:
            return ['0' * width]
        return ['0' + i for i in self.getPossibleStates(num, width - 1)] + \
               ['1' + i for i in self.getPossibleStates(num - 1, width - 1)]
    
    def convert(self, binary):
        h, m = int(binary[:4], 2), int(binary[4:], 2)
        if h > 11 or m > 59:
            return []
        return [str(h)+':'+('0' if m < 10 else '')+str(m)]
        
num = 1
print Solution().readBinaryWatch(num)

# first thought: need a generator for all possible states
