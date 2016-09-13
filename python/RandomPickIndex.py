# Given an array of integers with possible duplicates,
# randomly output the index of a given target number.

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        start, startstop = 0, count
        for num in count:
            # set the start and stop index of num
            # update start as the next avaliable index
            startstop[num], start = (start << 32) | start, start + count[num]

        indexes = [None] * len(nums)
        for i, num in enumerate(nums):
            indexes[startstop[num] & 0xFFFFFFFF] = i
            # add one to the stop index of num
            startstop[num] += 1

        self.indexes = indexes
        self.startstop = startstop

        # self.pick = lambda target: random.choice([i for i, num in enumerate(nums) if num == target])
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ss = self.startstop[target]
        return self.indexes[random.randrange(ss >> 32, ss & 0xFFFFFFFF)] # 4 byte
        
    
# each different number having its own list can be expensive
# an int takes only 24 bytes while even the empty list takes 72 bytes
# as you can see with print sys.getsizeof([]) and print sys.getsizeof(2**60)
