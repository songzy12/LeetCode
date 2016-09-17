# Shuffle a set of numbers without duplicates. 

class Solution(object):
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))

# reset: do not modify the origin array
# shuffle: random switch current position with following position
