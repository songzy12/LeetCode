# https://leetcode.com/problems/plus-one/description/


class Solution:

    def plusOne(self, digits):
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1

            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits = [carry] + digits
        return digits


if __name__ == "__main__":
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))
