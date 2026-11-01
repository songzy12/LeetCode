# https://leetcode.com/problems/multiply-strings/description/


class Solution:
    def multiply(self, num1, num2):
        # python 3.x unify long into int
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    print(Solution().multiply("123456789", "987654321"))
