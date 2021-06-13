class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        # get rid of the " " before or after
        # split the string into words
        t=s.strip(" ").split(" ")
        # find the last word
        # return its length
        return len(t[len(t)-1])
        #"a "
        #"b   a    "
        
for str in [""," ","a "," a"," a "," a  bc   "]:
    print (Solution().lengthOfLastWord(str))
