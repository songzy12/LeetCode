class Solution:
    # @return a string
    def convertToTitle(self, num):
##        if 1 <= num <= 26:
##            return chr(num + 64)
##        else:
##            if num % 26 == 0:
##                return ''.join([self.convertToTitle(num // 26 - 1),'Z'])
##            else:
##                return ''.join([self.convertToTitle(num // 26), chr(num % 26 + 64)])

        letters=[chr(x) for x in range(ord('A'),ord('Z')+1)]
        title=[]
        while num:
            num = num - 1
            title.append(letters[num % 26])
            num = num // 26
        title.reverse()
        return ''.join(title)
            

# AZ rather than B@
print(Solution().convertToTitle(52))
