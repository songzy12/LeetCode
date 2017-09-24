class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
##        left = {}
##        right = {}
##        ans = -1
##        length = len(flowers)
##        for i, flower in enumerate(reversed(flowers)):
##            has_left = flower > 1 and flower - 1 in left
##            has_right = flower < length and flower + 1 in right
##
##            if not has_left and not has_right:
##                left[flower] = flower - 1
##                right[flower] = flower + 1
##            elif has_left and has_right:
##                left[flower] = left[flower - 1]
##                right[flower] = right[flower + 1]
##                right[left[flower - 1] + 1] = right[flower]
##                left[right[flower + 1] - 1] = left[flower]
##            elif has_left and not has_right:
##                left[flower] = left[flower - 1]
##                right[flower] = flower + 1
##                right[left[flower - 1] + 1] = right[flower]
##            elif has_right and not has_left:
##                right[flower] = right[flower + 1]
##                left[flower] = flower - 1
##                left[right[flower + 1] - 1] = left[flower]
##
##            print flower, left[flower], right[flower], i
##            
##            if left[flower] >= 1 and right[flower] <= length and \
##               right[flower] - left[flower] - 1 == k:
##                ans = length - 1 - i
##
##        return ans

        days = [0 for i in range(len(flowers))]

        for i, flower in enumerate(flowers):
            days[flower - 1] = i + 1

        # print days
        
        ans = len(flowers) + 1

        left = 0
        right = k + 1

        for i in range(len(days)):
            if right >= len(days):
                break        
            if days[i] < days[left] or days[i] <= days[right]:
                if i == right:
                    ans = min(ans, max(days[left], days[right]))

                # if days[left] < days[i] > days[right], then i cannot be a left, since it will break at right.                
                
                left = i
                right = i + k + 1        

        return ans if ans < len(flowers) + 1 else -1
            

flowers = [10,1,6,4,2,8,9,7,5,3]
k = 1
print Solution().kEmptySlots(flowers, k)

# TreeSet
# Binary Index Tree
