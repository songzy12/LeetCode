class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        m = path.split('/')
        l = []
        for i in m:
            if i == '.' or i == '': # just ignore ''
                continue
            if i == '..':
                l = l[:-1]
            else:
                l.append(i)
##            if i == '..' and l: # check together
##                l.pop(-1)
##            elif i != '..': 
##                l.append(i)
        #print(l)
        return '/'+'/'.join(l)

path = "/a/b/.."
print(Solution().simplifyPath(path))
