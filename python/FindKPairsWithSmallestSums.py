# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        # Use at most the first k of each, then get the sizes.
        nums1 = nums1[:k]
        nums2 = nums2[:k]
        m, n = len(nums1), len(nums2)

        # Gotta Catch 'Em All?
        if k >= m * n:
            return [[a, b] for a in nums1 for b in nums2]
        
        # Build a virtual matrix.
        N, inf = max(m, n), float('inf')
        class Row:
            def __init__(self, i):
                self.i = i
            def __getitem__(self, j):
                return nums1[self.i] + nums2[j] if self.i < m and j < n else inf
        matrix = map(Row, range(N))

        # Get the k-th sum.
        kthSum = self.kthSmallest(matrix, k)

        # Discount the pairs with sum smaller than the k-th.
        j = min(k, n)
        for a in nums1:
            while j and a + nums2[j-1] >= kthSum:
                j -= 1
            k -= j

        # Collect and return the pairs.
        pairs = []
        for a in nums1:
            for b in nums2:
                if a + b >= kthSum + (k > 0):
                    break
                pairs.append([a, b])
                k -= a + b == kthSum
        return pairs

    def kthSmallest(self, matrix, k):
        # The median-of-medians selection function.
        def pick(a, k):
            if k == 1:
                return min(a)
            groups = (a[i:i+5] for i in range(0, len(a), 5))
            medians = [sorted(group)[len(group) / 2] for group in groups]
            pivot = pick(medians, len(medians) / 2 + 1)
            smaller = [x for x in a if x < pivot]
            if k <= len(smaller):
                return pick(smaller, k)
            k -= len(smaller) + a.count(pivot)
            return pivot if k < 1 else pick([x for x in a if x > pivot], k)

        # Find the k1-th and k2th smallest entries in the submatrix.
        def biselect(index, k1, k2):

            # Provide the submatrix.
            n = len(index)
            def A(i, j):
                return matrix[index[i]][index[j]]
            
            # Base case.
            if n <= 2:
                nums = sorted(A(i, j) for i in range(n) for j in range(n))
                return nums[k1-1], nums[k2-1]

            # Solve the subproblem.
            index_ = index[::2] + index[n-1+n%2:]
            k1_ = (k1 + 2*n) / 4 + 1 if n % 2 else n + 1 + (k1 + 3) / 4
            k2_ = (k2 + 3) / 4
            a, b = biselect(index_, k1_, k2_)

            # Prepare ra_less, rb_more and L with saddleback search variants.
            ra_less = rb_more = 0
            L = []
            jb = n   # jb is the first where A(i, jb) is larger than b.
            ja = n   # ja is the first where A(i, ja) is larger than or equal to a.
            for i in range(n):
                while jb and A(i, jb - 1) > b:
                    jb -= 1
                while ja and A(i, ja - 1) >= a:
                    ja -= 1
                ra_less += ja
                rb_more += n - jb
                L.extend(A(i, j) for j in range(jb, ja))
                
            # Compute and return x and y.
            x = a if ra_less <= k1 - 1 else \
                b if k1 + rb_more - n*n <= 0 else \
                pick(L, k1 + rb_more - n*n)
            y = a if ra_less <= k2 - 1 else \
                b if k2 + rb_more - n*n <= 0 else \
                pick(L, k2 + rb_more - n*n)
            return x, y

        # Set up and run the search.
        n = len(matrix)
        start = max(k - n*n + n-1, 0)
        k -= n*n - (n - start)**2 # if start == 0, then k unchanged
        return biselect(range(start, min(n, start+k)), k, k)[0]

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print Solution().kSmallestPairs(nums1, nums2, k)

# ht tps://discuss.leetcode.com/topic/53126/o-n-from-paper-yes-o-rows
# https://discuss.leetcode.com/topic/53380/o-k-solution 
