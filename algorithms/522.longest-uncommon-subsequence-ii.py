class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs:
            return -1

        strs.sort(key=lambda x: (len(x), x), reverse=True)
        temp = strs[0]
        count = 1
        negative = []
        def check(temp):
            def check_(temp, x):
                # return if temp is subsequence of x
                if len(temp) >= len(x):
                    return False
                q = iter(x)
                for p in temp:
                    if p not in q:
                        return False
                return True
                        
            for x in negative:
                if check_(temp, x):
                    return False
            return True

        for i in range(1, len(strs)):
            if strs[i] == temp:
                count += 1
            else:
                if count == 1 and check(temp):
                    return len(temp)
                negative += [temp]
                count = 1
                temp = strs[i]
        if count == 1 and check(temp):
            return len(temp)
        return -1

if __name__ == '__main__':
    strs = ["a","b","c","d","e","f","a","b","c","d","e","f"]
    print Solution().findLUSlength(strs)
