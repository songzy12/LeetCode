# https://leetcode.com/problems/multiply-strings/description/


class Solution:

    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]

        res = []
        for i in range(len(num2)):
            num = "0" * i + self.multiply_single(num1, int(num2[i]))
            res.append(num)

        res = self.sum_all(res)

        return self.normalize(res)

    def multiply_single(self, num, digit):
        res = []
        carry = 0
        for n in num:
            total = int(n) * digit + carry
            res.append(total % 10)
            carry = total // 10

        if carry:
            res.append(carry)
        return "".join([str(d) for d in res])

    def sum_all(self, nums):
        max_len = max(len(num) for num in nums)
        carry = 0
        res = []
        for i in range(max_len):
            total = carry
            for num in nums:
                if i < len(num):
                    total += int(num[i])
            res.append(total % 10)
            carry = total // 10

        if carry:
            res.append(carry)
        return "".join([str(d) for d in res])

    def normalize(self, res):
        res = res[::-1]
        res = res.lstrip("0")
        if not len(res):
            return "0"
        return res


if __name__ == "__main__":
    print(Solution().multiply("123456789", "987654321"))
    print(Solution().multiply("1234", "0"))
    print(Solution().multiply("408", "5"))
