class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # find the axis first
        # it is the min of two
        if len(n) == 1:
            return str(int(n)-1)
        def get_greater(n):
            len_ = len(n)
            head = n[:len_/2]
            if len_ % 2:
                # odd
                if int(head+n[len_/2]+head[::-1]) > int(n):
                    return head+n[len_/2]+head[::-1]
                head = str(int(head+n[len_/2])+1)
                if len(head) > len_/2 + 1:
                    return '1'+'0'*(len_-1) + '1'
                return head+head[:-1][::-1]
            else:
                if int(head+head[::-1]) > int(n):
                    return head+head[::-1]
                head = str(int(head)+1)
                if len(head) > len_/2:
                    return '1'+'0'*(len_-1) + '1'
                return head+head[::-1]

        def get_smaller(n):
            len_ = len(n)
            head = n[:len_/2]
            if len_ % 2:
                # odd
                if int(head+n[len_/2]+head[::-1]) < int(n):
                    return head+n[len_/2]+head[::-1]
                head = str(int(head+n[len_/2])-1)
                if len(head) < len_/2 + 1 or not int(head):
                    return '9'*(len_-1)
                return head+head[:-1][::-1]
            else:
                if int(head+head[::-1]) < int(n):
                    return head+head[::-1]
                head = str(int(head)-1)
                if len(head) < len_/2 or not int(head):
                    return '9'*(len_-1)
                return head+head[::-1]
            
        def choose(n, a, b):
            if abs(n-a) < abs(n-b):
                return a
            if abs(n-a) > abs(n-b):
                return b
            return min(a, b)
        print int(n), int(get_greater(n)), int(get_smaller(n))
        ans = choose(int(n), int(get_greater(n)), int(get_smaller(n)))
        return str(ans)
        
n = "1"
print Solution().nearestPalindromic(n)

# not including itself

# "10"->"9", rather than '10'->'00'
# '98'->'99', rahter than '98'->'1001'

# '1'->'0', rather than '1'->''
