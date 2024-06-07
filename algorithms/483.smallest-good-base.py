class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        max_m = int(math.log(n,2)) # Refer [7]
        for m in range(max_m,1,-1):
            k = int(n**m**-1)  # Refer [6]
            if (k**(m+1)-1)//(k-1) == n:
                # Refer [3]
                return str(k)
        
        return str(n-1)  
        
# I have seen this before.
# iterate through the length of representation 1...1
# then check whether there is a suitable base using binary search
