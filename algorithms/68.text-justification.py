class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        text = ' '.join(words)+' '
        if text == ' ':
            return [' '*L]
        res = []
        while text:
            idx = text.rfind(' ', 0, L+1)
            line = text[:idx].split()
            l, n = sum(len(w) for w in line), len(line)
            if n == 1:
                res.append(line[0].ljust(L))
            else:
                s, remainder = divmod(L-l, n-1)
                line[:-1] = [w+' '*s for w in line[:-1]]
                line[:remainder] = [w+' ' for w in line[:remainder]]
                res.append(''.join(line))
            text = text[idx+1:]
        res[-1] = ' '.join(res[-1].split()).ljust(L)
        return res
##        if len(words)==1:
##            return [words[0] + " " * (L - len(words[0]))]
##        index = 1
##        string = ""
##        numSpace = index - 1
##        lenWord = len(words[0])
##        while lenWord + len(words[index]) + numSpace + 1 <= L:
##            lenWord += len(words[index])
##            numSpace += 1
##            index += 1
##            if index == len(words):
##                break
##        if index == len(words):
##            for i in range(index):
##                string+=words[i]
##                if i!=index-1:
##                    string += " "
##                else:
##                    string += " " * (L - lenWord - i)
##            return [string]
##        if index == 1:
##            return [words[0] + " " * (L - len(words[0]))]+self.fullJustify(words[index:], L)
##        lenSpaceSum = L - lenWord
##        lenSpaceEach = lenSpaceSum // numSpace
##        lenSpaceLeft = lenSpaceSum % numSpace
##        for i in range(index):
##            string += words[i]
##            if i != index-1:
##                string += " "*(lenSpaceEach+1) if i < lenSpaceLeft else " "*lenSpaceEach
##        return [string]+self.fullJustify(words[index:], L)
            

words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
words = ['a','b','c','d','e']
L = 1
words = ['']
L = 2
words = ["Listen","to","many,","speak","to","a","few."]
L = 6
words = ["What","must","be","shall","be."]
L = 12
print(Solution().fullJustify(words, L))

##[
##   "This    is    an",
##   "example  of text",
##   "justification.  "
##]
