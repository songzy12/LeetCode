class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return 'Zero'
        ans = []
        suffix = ['', 'Thousand', 'Million', 'Billion']
        word = ['Zero', 'One', 'Two', 'Three', 'Four',
                'Five', 'Six', 'Seven', 'Eight', 'Nine',
                'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                'Fifteen','Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
                'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
                'Seventy', 'Eighty', 'Ninety']  # Ninety
        suf = 0
        while num:
            tempWord, tempNum = [], num%1000
            if tempNum // 100:
                tempWord += word[tempNum // 100], 'Hundred',
            tempNum %= 100
            if tempNum:
                if tempNum < 20:
                    tempWord += word[tempNum],
                else:
                    tempWord += word[20+(tempNum-20)//10],
                    if tempNum % 10:
                        tempWord += word[tempNum%10],
            # 1000000, 1001
            ans = tempWord + [suffix[suf]] + \
                  (ans[1:] if suf and ans[0] == suffix[suf-1] else ans)
            # print ans
            num //= 1000
            suf += 1
        return ' '.join(ans).strip()

import random
print Solution().numberToWords(123)
for i in range(10):
    num = random.randint(1, 2**31-1)
    print num, Solution().numberToWords(num)
