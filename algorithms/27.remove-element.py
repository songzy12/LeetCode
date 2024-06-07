class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        # the oj will truc list to be the length
        while elem in A:
            A.remove(elem)
        return len(A)

# if use for x in A, then there will be some error
A=[3,3]
elem=3
print(Solution().removeElement(A,elem))
