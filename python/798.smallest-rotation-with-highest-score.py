class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            A[i] -= i

        # print(A)
        # we want A[i] <= 0
        def rotate(k, i):
            A[i] += k
            if i < k:
                A[i] -= len(A)
            return A[i]

        def get_range(i):
            maxi = A[i] + i
            mini = A[i] - len(A) + i + 1
        
            if mini > 0:
                return []
            if maxi <= 0:
                return [[0, len(A)-1]]

            index_0 = maxi
            if index_0 > i:
                return [[i + 1, i + 1 - mini]]
            else:
                if i + 1 <= len(A) - 1:
                    return [[0, -A[i]], [i + 1, len(A)-1]]
                else:
                    return [[0, -A[i]]]

        prefix = [0 for i in range(len(A)+1)]
        for i in range(len(A)):
            ranges = get_range(i)
            # print(i, ranges)
            for left, right in ranges:
                prefix[left] += 1
                prefix[right + 1] -= 1

        index = 0
        score = prefix[0]
        prefix_sum = score
        for i in range(1, len(A)):
            prefix_sum += prefix[i]
            if prefix_sum > score:
                index = i
                score = prefix_sum
        return index

A = [2, 3, 1, 4, 0]
A = [1, 3, 0, 2, 4]
print(Solution().bestRotation(A))
            
            
