class Solution:
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        seperator = ['(', ')', ' ']
        operator = ['add', 'let', 'mult']

        def next_token(s):
            if s[0] in seperator:
                return s[0]
            temp = []
            i = 0
            while i < len(s) and s[i] not in seperator:
                temp.append(s[i])
                i += 1
            token = ''.join(temp)
            return token

        def next_exp(s):
            if s[0] != '(':
                return next_token(s)
            stack = [s[0]]
            i = 1
            while stack and i < len(s):
                if s[i] == '(':
                    stack.append('(')
                if s[i] == ')':
                    stack.pop(-1)
                i += 1
                
            return s[:i]
        
        def _eval(s, m):
            print('_eval:', s)
            index = 0
            
            token = next_token(s)
            index += len(token)

            if token not in seperator:
                if token in m:
                    return m[token]
                return int(token)

            token = next_token(s[index:])
            index += len(token)

            if token not in operator:
                if token in m:
                    return m[token]
                return int(token)

            if token != 'let':
                index += 1
                exp1 = next_exp(s[index:])
                
                index += len(exp1)
                index += 1
                exp2 = next_exp(s[index:])

                print(token, 'exp:', exp1, exp2)
                
                if token == 'mult':
                    return _eval(exp1, m) * _eval(exp2, m)
                else:
                    return _eval(exp1, m) + _eval(exp2, m)
            else:
                m_copy = dict(m)
                index += 1
                
                token = next_token(s[index:])
                while token != ')':
                    
                    if token != '(':
                        index += len(token)
                        index += 1
                        try:
                            exp = next_exp(s[index:])
                        except:
                            if token in m_copy:
                                return m_copy[token]
                            return int(token)
                        print('let token:', token, exp)
                        index += len(exp)
                        index += 1
                        
                        m_copy[token] = _eval(exp, m_copy)
                        token = next_token(s[index:])
                    else:
                        exp = next_exp(s[index:])
                        print("let eval:"+exp)
                        return _eval(exp, m_copy)

        m = {}
        return _eval(expression, m)

s = '(let x 2 (mult x (let x 3 y 4 (add x y))))'
print (Solution().evaluate(s))
