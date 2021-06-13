class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.restoreIpAddressesHelper(s, len(s), 4)
    def restoreIpAddressesHelper(self, s, left, layer):
        if left == 0 or left > 3*layer:
            return []
        if layer == 1:
            if left > 1 and s[-left] == '0' or int(s[-left:]) > 255:
                return []
            else:
                return [s[-left:]]
        ans = []
        if left > 1:
            temp = self.restoreIpAddressesHelper(s, left-1, layer-1)
            if temp:
                ans += [s[-left] + '.' + i for i in temp]
        if left > 2 and 10 <= int(s[-left:-left+2]):
            temp = self.restoreIpAddressesHelper(s, left-2, layer-1)
            if temp:
                ans += [s[-left:-left+2]+'.'+ i for i in temp]
        if left > 3 and 100 <= int(s[-left:-left+3]) <= 255:
            temp = self.restoreIpAddressesHelper(s, left-3, layer-1)
            if temp:
                ans += [s[-left:-left+3]+'.'+ i for i in temp]
        return ans

s = "010010"
print Solution().restoreIpAddresses(s)
        
