# https://leetcode.com/problems/add-binary/description/


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))
