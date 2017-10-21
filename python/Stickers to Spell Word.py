import code
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        from string import ascii_lowercase

        def convert(x):
            return tuple([x.count(y) for y in ascii_lowercase])
        
        stickers = map(convert, stickers)
        target = convert(target)
        
        dp = {} 
        
        def get_dp(target):
            if target in dp:
                return dp[target]
            if max(target) == 0:
                return 0
            
            res = -1

            head = 0
            while not target[head]:
                head += 1
                
            for sticker in stickers:

                if not sticker[head]: # this is important for TLE, and do not use Counter
                    continue
                
                target0 = [0 for i in range(26)]
                for i in range(26):
                    target0[i] = max(0, target[i] - sticker[i])

                temp = get_dp(tuple(target0))
                
                if temp != -1 and (res == -1 or temp < res):
                    res = temp

            dp[target] = res + 1 if res != -1 else -1
            return dp[target]
        
        return get_dp(target)
            
            
stickers, target = ["seven","old","stream","century","energy","period","an","proper","together","sight","carry","milk","appear","winter","field","rather","caught","danger","lake","shall","machine","few","other","test","got","wing","map","finish","though","observe","log","they","foot","path","eat","glad","must","bar","did","of","clear","work","rule","quotient","produce","clean","wild","grass","example","left"],"weresurprise"
print Solution().minStickers(stickers, target)
        
# whether the state of 50**26 too many?
# TLE
