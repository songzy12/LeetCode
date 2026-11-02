# https://leetcode.com/problems/add-binary/description/


class Solution:

    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]

        c = ""
        carry = 0

        index = 0
        while index < len(a) and index < len(b):
            total = int(a[index]) + int(b[index]) + carry
            c += str(total % 2)
            carry = total // 2
            index += 1
        while index < len(a):
            total = int(a[index]) + carry
            c += str(total % 2)
            carry = total // 2
            index += 1
        while index < len(b):
            total = int(b[index]) + carry
            c += str(total % 2)
            carry = total // 2
            index += 1
        if carry:
            c += str(carry)

        return c[::-1]


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))
