class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = n2 = 0
        c1 = c2 = 0
        for num in nums:
            if c1 and c2:
                if num == n1:
                    c1 += 1
                elif num == n2:
                    c2 += 1
                else:
                    c1 -= 1
                    c2 -= 1
            elif c1:
                if num == n1:
                    c1 += 1
                else:
                    n2 = num
                    c2 += 1
            elif c2:
                if num == n2:
                    c2 += 1
                else:
                    n1 = num
                    c1 += 1
            else:
                n1 = num
                c1 += 1
        c1 = c2 = 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
        return ([n1] if c1 > len(nums)//3 else []) +\
               ([n2] if c2 > len(nums)//3 else [])

nums = []
print Solution().majorityElement(nums)
    
        
                    
                    
