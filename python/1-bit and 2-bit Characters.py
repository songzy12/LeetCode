class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        def valid(bits):
            i = 0
            while i < len(bits):
                if bits[i] == 0:
                    i += 1
                else:
                    i += 2
            return i == len(bits)
        return valid(bits[:-1])
