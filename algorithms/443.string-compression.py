class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        cur = 0
        while i < len(chars):
            t = 0
            while i + t < len(chars) and chars[i + t] == chars[i]:
                t += 1
            if t == 1:
                chars[cur] = chars[i] 
                i += t
                cur += t
                continue
            else:
                part = list(chars[i]+str(t))
                for j, c in enumerate(part):
                    chars[cur + j] = c

                cur += len(part)
                i += t
        return cur

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print Solution().compress(chars)
print chars
