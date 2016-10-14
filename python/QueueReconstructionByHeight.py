# Each person is described by a pair of integers (h, k), 
# where h is the height of the person and 
# k is the number of people in front of this person 
# who have a height greater than or equal to h. 
# Write an algorithm to reconstruct the queue. 

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: (x[0], -x[-1]))
        
        ans = [None for i in range(len(people))]
        emp = [i for i in range(len(people))]
        for h, k in people:
            t = emp[k]
            # emp.pop(k)
            emp.remove(t)
            # [[7,0], [7,1]] should be sorted to [[7,1], [7,0]]
            ans[t] = [h, k]
        return ans

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print Solution().reconstructQueue(people)