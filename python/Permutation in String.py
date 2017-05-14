class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        from collections import Counter
        target = Counter(s1)
        current = Counter(s2[:len(s1)])
        if current == target:
            return True

        i = len(s1)
        while i < len(s2):            
            current[s2[i]] += 1
            current[s2[i-len(s1)]] -= 1
            if not current[s2[i-len(s1)]]:
                current.pop(s2[i-len(s1)])
            if current == target:
                return True            
            i += 1
        return False
        
s1 = 'ab'
s2 = 'eidboaoo'
print Solution().checkInclusion(s1, s2)
