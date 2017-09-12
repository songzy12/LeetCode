class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        m = {}
        max_sum = len(list1) + len(list2)
        ans = []
        for i, item in enumerate(list1):
            m[item] = i
        for i, item in enumerate(list2):
            if item in m:
                temp = i + m[item]
                if temp < max_sum:
                    max_sum = temp
                    ans = [item]
                elif temp == max_sum:
                    ans.append(item) # return a list
        return ans
