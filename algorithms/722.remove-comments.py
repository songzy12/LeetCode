class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        ans = []
        flag = False
        temp = ''
        for line in source:
            i = 0
            while i < len(line):
                if flag:
                    if i < len(line) - 1 and line[i] == '*' and line[i+1] == '/':
                        flag = False
                        i += 2
                        continue
                    i += 1
                else:
                    if i < len(line) - 1 and line[i] == '/' and line[i+1] == '*':
                        flag = True
                        i += 2
                        continue
                    elif i < len(line) - 1 and line[i] == line[i+1] == '/':
                        i = len(line)
                        continue
                    else:
                        temp += line[i]
                        i += 1
            if temp and not flag:
                ans.append(temp)
                temp = ''
        return ans

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print '\n'.join(Solution().removeComments(source))

# remember that is /* rather than \*
