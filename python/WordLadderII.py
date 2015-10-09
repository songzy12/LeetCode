class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        path = []
        res = []
        if start == end:
            path.append(end)
            res.append(path)
            return res
        dict.add(start)
        dict.add(end)
        
        edge = {}
        for word in dict:
            edge[word] = []
        for word in dict:
            for i in range(len(word)):
                for c in range(97, 123):
                    nw = word[:i] + chr(c) + word[i+1:]
                    if nw in dict:
                        edge[word].append(nw)

##        for i in edge:
##            print(i, edge[i])

        queue = [[start]]
        flag = 0
        delete = set([start])
        size = 1
        add = []
        while len(queue):
            words = queue.pop(0) 
            if flag and len(words) >= flag: # res not empty
                break
            if len(words) > size:
                size = len(words)
                delete |= set(add)
                add = []
            word = words[-1]
            for nw in edge[word]:
                if nw == end:
                    flag = len(words) + 1
                    res.append(words + [nw])
                if nw not in delete:
                    queue.append(words + [nw])
                    add.append(nw)
        return res
    
start = "hit"
end = "cog"
dict = set(["hot","dot","dog","lot","log"])
print(Solution().findLadders(start, end, dict))
'''
[
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
]
'''
