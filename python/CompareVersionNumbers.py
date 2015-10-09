class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
##        v1 = version1.split('.')
##        v2 = version2.split('.')
##        for i in range(len(v1)):
##            if i > len(v2)-1:
##                if int(v1[i])>0: 
##                    return 1
##                else:
##                    return 0
##            if int(v1[i])>int(v2[i]):
##                return 1
##            if int(v1[i])<int(v2[i]):
##                return -1
##        if i < len(v2)-1 and int(v2[i+1])>0:
##            return -1
##        return 0

        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)
        l = max(l1, l2)
        for i in range(l):
            n1 = int(v1[i]) if i<l1 else 0
            n2 = int(v2[i]) if i<l2 else 0
            if n1 > n2:
                return 1
            if n1 < n2:
                return -1
        return 0
    
#version1='1'
#version2='1.1'
#version1='01'
#version2='1'
#version1='1.0'
#version2='1'
version1='1'
version2='1.0'

print(Solution().compareVersion(version1, version2))

