# Given an array of integers representing the data,
# return whether it is a valid utf-8 encoding.


class Solution(object):    
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        
        self.data = map(lambda x: x & 0xff, data)
        index = 0
        while index < len(self.data):
            n = 7 # 1 << n is of length n+1
            while n >= 0 and self.data[index] & 1<<n: 
                n -= 1 # bin(data) can get the binary form of data
            n = 7 - n
            if n == 1: # it is not valid to get length 1
                return False
            elif n == 0:
                n = 1
            
            if len(self.data) < index + n:
                return False
            for i in range(index + 1, index + n):
                if self.data[i] & 0xc0 != 0x80:
                    return False
            index += n
        return True
        
data = [197,130,1]
print Solution().validUtf8(data)
