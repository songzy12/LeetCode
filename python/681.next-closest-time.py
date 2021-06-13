class Solution(object):

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = set(''.join(time.split(":")))
      
        def check(time):
            h, m = map(int, time.split(":"))
            if h > 23 or m > 59:
                return False
            return True
        
        def possible(nums):
            res = []
            for h0 in nums:
                for h1 in nums:
                    for sep in [":"]:
                        for m0 in nums:
                            for m1 in nums:
                                time = h0+h1+sep+m0+m1
                                if not check(time):
                                    continue
                                res.append(time)
            return res
        
        pos_times = possible(nums)

        def diff(time0, time1):
            h0, m0 = map(int, time0.split(":"))
            h1, m1 = map(int, time1.split(":"))
            if h0 > h1 or h0 == h1 and m0 > m1:
                h1 += 24
            if m1 < m0:
                m1 += 60
                h1 -= 1
            ans = (h1 - h0) * 60 + m1 - m0
            if not ans:
                return 24 * 60
            return ans

        ans_time = time
        ans_diff = 24 * 60
        for pos_time in pos_times:
            cur_diff = diff(time, pos_time)
            if cur_diff < ans_diff:
                ans_diff = cur_diff
                ans_time = pos_time
        return ans_time
    
time = "00:00"
print Solution().nextClosestTime(time)
            
        
