class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        medians = []
        hash_ = {}
        bheap = [] # bottom half, max-heap
        from heapq import heappop, heappush, heapify
        theap = nums[:k] # top half, min-heap
        heapify(theap)
        for i in range(k/2): # theap is one more than bheap
            heappush(bheap, -heappop(theap)) # bheap is max-heap
        len_nums = len(nums)
        for i in range(k, len_nums+1):
            if k % 2:
                medians += theap[0],
            else:
                medians += (theap[0]-bheap[0])/2.0,
            if i == len_nums:
                break
            
            m = nums[i-k]
            n = nums[i]
            balance = 0
            
            # remove m
            if bheap and m <= -bheap[0]: # remember to check whether empty before do something
                balance -= 1 # remove m from bheap
                if m == -bheap[0]:
                    heappop(bheap)
                else:
                    hash_[m] = hash_.get(m,0)+1
            else:
                balance += 1 # remove m from theap
                if m == theap[0]:
                    heappop(theap)
                else:
                    hash_[m] = hash_.get(m,0)+1
                    
            # add n
            if bheap and n <= -bheap[0]:
                balance += 1
                heappush(bheap, -n)
            else:
                balance -= 1
                heappush(theap, n)
            
            # rebalance
            if balance < 0: 
                heappush(bheap, -heappop(theap))
            elif balance > 0:
                heappush(theap, -heappop(bheap))
            
            while bheap and hash_.get(-bheap[0],0):
                hash_[-bheap[0]] -= 1 # be careful with the order of operations
                heappop(bheap)
            while theap and hash_.get(theap[0],0):
                hash_[theap[0]] -= 1
                heappop(theap)
        return map(float,medians)
        
# first thought: use two heaps, one min-heap and one max-heap
# while it is not suitable for delete operation (?)

# solution: we only delete it when it comes to the top
# while we descrese the count of that heap
