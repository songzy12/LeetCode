# We call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.

'''
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted([2*num for num in nums])
        ans = 0
        from bisect import bisect_left
        for num in nums:
            # find number of e, s.t. 2*num > e
            temp.remove(2*num)
            # print temp, num, bisect_left(temp, num)
            ans += bisect_left(temp, num)
        return ans
'''

class Solution(object):
    def __init__(self):
        self.cnt = 0
    def reversePairs(self, nums):
        def msort(h, lst):          # h: beginning index of list
            # merge sort body
            L = len(lst)
            if L <= 1:                          # base case
                return lst
            else:                               # recursive case, pass the original index to merger
                return merger(h, msort(h, lst[:int(L/2)]), msort(h+int(L/2), lst[int(L/2):]))
        def merger(s, left, right):
            # merger
            new, l, r = [], 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= 2*right[r]: # this is the only difference with reverse pair
                    l += 1
                else:
                    self.cnt += len(left)-l       # count here
                    r += 1
            return sorted(left+right)    # I can't avoid TLE without timsort...

        msort(0, nums)
        return self.cnt

# it is a divide and conquer method
# we divide the total number as three parts: 
# the first half, the second half, the pairs in between
# then we use the merge step to count the third part
# we use the sort step to count the first two parts

nums = [2,4,3,5,1]
print Solution().reversePairs(nums)

'''
class Solution(object):
    def reversePairs(self, nums):
        root = None
        cnt = [0]
        for i in range(len(nums)-1, -1, -1):
            self.search(cnt, root, nums[i]/2.0)
            root = self.build(nums[i], root)
        return cnt[0]

    def search(self, cnt, node, target):
        if not node:
            return
        if target == node.val:
            cnt[0] += node.less
        elif target < node.val:
            self.search(cnt, node.left, target)
        else:
            cnt[0] += (node.less + node.same)
            self.search(cnt, node.right, target)

    def build(self, val, n):
        if not n:
            return TreeNode(val)
        elif val == n.val:
            n.same += 1
        elif val > n.val:
            n.right = self.build(val, n.right)
        else:
            n.less += 1
            n.left = self.build(val, n.left)
        return n
'''