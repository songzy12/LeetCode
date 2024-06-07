# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        temp = rand7()
        while temp == 7:
            temp = rand7()
            
        temp2 = rand7()
        while temp2 > 5:
            temp2 = rand7()
        return temp2 + (temp % 2) * 5
