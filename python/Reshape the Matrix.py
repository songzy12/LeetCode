class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp = []
        for row in nums:
            temp += row
        if r * c != len(temp):
            return nums
        ans = []
        for i in range(r):
            ans.append(temp[i*c:(i+1)*c])
        return ans
