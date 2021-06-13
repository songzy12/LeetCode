class Solution:
    def findSubstring(self, s, wrods):

        ans = []
        n, cnt = len(s), len(words)
        if n <= 0 or cnt <= 0:
            return ans
        d = dict()
        for i in words:
            d[i] = d.get(i, 0) + 1
        
        wl = len(words[0])
        # off set of window 
        for i in range(wl):
            left, count = i, 0
            td = dict()
            # window length controlled by count
            for j in range(i, n-wl+1, wl):
                sub = s[j:j+wl]
                if d.has_key(sub):
                    td[sub] = td.get(sub, 0)+1
                    if td[sub] <= d[sub]:
                        count += 1
                    else:
                        while td[sub] > d[sub]:
                            s1 = s[left: left + wl]
                            td[s1] -= 1
                            if td[s1] < d[s1]:
                                count -= 1
                            left += wl
                    if count == cnt:
                        ans += left,
                        td[s[left:left+wl]] -= 1
                        count -= 1
                        left += wl
                else:
                    td.clear()
                    count = 0
                    left = j + wl
        return ans

##    def findSubstring(self, s, words):
##        n = len(words)    
##        w = len(words[0])  
##        t = n*w    
##        hashsum = sum([hash(x) for x in words])
##        h = [hash(s[i:i+w])*(s[i:i+w] in words) for i in xrange(len(s)-w+1)]
##        return [i for i in xrange(len(s)-t+1) if sum(h[i:i+t:w])==hashsum]

s = "barfoothefoobarman"
words = ["foo","bar"]
print Solution().findSubstring(s, words)
