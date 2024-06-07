class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        numstack = []
        opstack = []
        i = len(s) -1
        while i > -1:
            if s[i] in '0123456789':
                j  = i
                while  i > -1 and s[i] in '0123456789':
                    i -= 1
                i += 1
                numstack.append(int(s[i:j+1]))
            else:
                if s[i] in ')+-':
                    opstack.append(s[i])
                if s[i] == '(':
                    while opstack[-1] != ')':
                        if opstack.pop() == '+':
                            numstack.append(numstack.pop()+numstack.pop())
                        else:
                            numstack.append(numstack.pop()-numstack.pop())
                    opstack.pop()
            i -= 1 # push from back, calc from head
        while opstack:
            if opstack.pop()=='+':
                numstack.append(numstack.pop()+numstack.pop())
            else:
                numstack.append(numstack.pop()-numstack.pop())
        return numstack[-1]
    
s = '(2 + 3 ) - (1+2)'
print(Solution().calculate(s))
