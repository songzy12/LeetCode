# https://leetcode.com/problems/add-strings/description/


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        max_len = max(len(num1), len(num2))
        carry = 0
        res = ""
        for i in range(max_len):
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[i]) if i < len(num2) else 0
            total = n1 + n2 + carry
            res += str(total % 10)
            carry = total // 10

        if carry:
            res += str(carry)

        return res[::-1]
