class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if not tokens:
            return None
        l = []
        for i in tokens:
            # print(l)
            if i not in ['+','-','*', '/']:
                l += [int(i)]
                continue
            t1 = l.pop()
            t2 = l.pop()
            if i == '+':
                l += [t1 + t2]
            elif i == '-':
                l += [t2 - t1]
            elif i == '*':
                l += [t2 * t1]
            else:
                # long but right
                # l += [abs(t2) // abs(t1) * (1 if t2*t1>0 else -1)]
                l += [int(float(t2) / t1)]
        return l[0]

tokens = ['2','1','+','3','*']
tokens = ['4', '13', '5', '/', '+']
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["4","-2","/","2","-3","-","-"]
# 6//-132 = -1
print(Solution().evalRPN(tokens))
