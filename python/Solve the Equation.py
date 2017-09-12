import re
class Solution(object):
    def solveEquation(self, equation):
        x = a = 0
        side = 1
        for eq, sign, num, isx in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                x += side * int(sign + '1') * int(num or 1) # since here 0 is '0'
            elif num:
                a -= side * int(sign + num)
        return 'x=%d' % (a / x) if x else 'No solution' if a else 'Infinite solutions'

'''
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        equation = list(equation)
        equation += ['+', '0']
        index = 0
        
        def next_token(index):
            if equation[index] in ['+', '-', '=', 'x']:
                return equation[index]
            temp = []
            while index < len(equation) and equation[index] not in ['+', '-', '=', 'x']:
                temp += equation[index],
                index += 1
            return ''.join(temp)

        coef = 0
        const = 0
      
        left = 1
        sign = 1
        number = 0

        flag = False # difference between 0x and x

        # maintain the above variables at each step
        while index < len(equation):
            token = next_token(index)
            index += len(token)
            
            if token == '+':
                const += number*sign*left
                number = 0
                sign = 1
                flag = False
            elif token == '-':
                const += number*sign*left
                number = 0
                sign = -1
                flag = False
            elif token == '=':
                const += number*sign*left
                number = 0
                sign = 1
                left = -1
                flag = False
            elif token == 'x':
                if flag:
                    coef += number*sign*left
                else:
                    coef += sign * left
                number = 0
                sign = 1
                flag = False
            else:
                number = int(token)
                flag = True

            # print token, coef, const

        def solve(coef, const):
            if coef:
                return "x="+str(-const / coef)
            if not const:
                return "Infinite solutions"
            return "No solution"

        # print coef, const
        
        return solve(coef, const)
'''

for equation  in ['1+1=x', '-x=-1', 'x+5-3+x=6+x-2', 'x=x', '2x=x',
                  '2x+3x-6x=x+2', 'x=x+2', '2=-x', '0x=0']:

    print Solution().solveEquation(equation)

# x=2
# x=1
# x=2
# Infinite solutions
# x=0
# x=-1
# No solution
# x=-2
# Infinite solutions


'''
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def helper(s):
            sign, n = 1, len(s)
            # i, coef, const stand for current index, and accumulative 'x' coefficient and constant
            i = coef = const = 0
            while i < n:
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i].isdigit():
                    j = i
                    while j < n and s[j].isdigit():
                        j += 1
                    tmp = int(s[i:j])
                    if j < n and s[j] == 'x':
                        coef += tmp * sign # here resolve the 0x and x condition
                        j += 1
                    else:
                        const += tmp * sign
                    i = j-1
                else:
                    coef += 1 * sign
                i += 1
            return coef, const
            
        left, right = equation.split('=')
        k1, b1 = helper(left)
        k2, b2 = helper(right)
        # k1x + b1 = k2x + b2
        ans = 'x=' + str((b2 - b1) / (k1 - k2)) if k1 != k2 and b1 != b2 \
              else "Infinite solutions" if k1 == k2 and b1 == b2 \
              else "No solution" if b2 != b1 else 'x=0'
        return ans
'''

'''
def solveEquation(self, equation):
    z = eval(equation.replace('x', 'j').replace('=', '-(') + ')', {'j': 1j})
    a, x = z.real, -z.imag
    return 'x=%d' % (a / x) if x else 'No solution' if a else 'Infinite solutions'
'''
