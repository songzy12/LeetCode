class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_num(nums):
            l = []
            i = 0
            while i < len(nums) and (not l or nums[i] >= l[-1]):
                l.append(nums[i])
                i += 1
            while i < len(nums):
                while l and nums[i] < l[-1]: 
                    l.pop(-1)
                i += 1
            return len(l)
        temp = len(nums) - get_num(nums) - get_num(map(lambda x: -x, nums[::-1]))
        return temp if temp > 0 else 0

if __name__ == '__main__':
    nums = [1,2,3,4]
    print Solution().findUnsortedSubarray(nums)
            
# check l before l[-1]
# temp may be less than 0
