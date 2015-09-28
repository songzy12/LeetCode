class Solution(object):
    def compare(self, a, b):
        length = min(len(a), len(b))
        i = 0
        while i<length:
            if a[i] != b[i]:
                return  int(b[i])-int(a[i])
            i += 1
        if length < len(b): # [121, 12]
            return self.compare(a, b[length:])
        elif length < len(a):
            return self.compare(a[length:], b)
        else:
            return 0
        
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted(map(lambda i:str(i),nums), cmp = lambda x, y: self.compare(x, y))
        return str(int(''.join(nums)))
      
nums = [0, 0]
print Solution().largestNumber(nums)
        
