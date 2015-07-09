class Solution:
    # @param str, a string
    # @return an integer
    def myAtoi(self, str):
        str = str.strip()
        temp = ''
        sign = False
        for i in str:
            if i in '-+':
                if not sign:
                    sign = True
                    temp += i
                    continue
                return 0
            if i in '0123456789':
                temp += i
                continue
            break

        if len(temp) == 0 or len(temp)==1 and temp[0] in '+-':
            return 0
        result = int(temp)
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return int(temp)

for str in '', '+-2', '+0 123', '2147483648':
    print(Solution().myAtoi(str))
