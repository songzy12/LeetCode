class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # notice the difference of split() and split(' ')
        s=s.split()
        s.reverse()
        return ' '.join(s)

##        import re
##        s=re.split('\s+',s.strip())
##        s.reverse()
##        return ' '.join(s)

for s in 'the sky is blue',' ','  a     b':
    print(Solution().reverseWords(s))
