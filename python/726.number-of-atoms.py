# https://leetcode.com/problems/number-of-atoms/description/
# https://leetcode.com/problemset/algorithms/?difficulty=Hard&status=Todo


class Solution:

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [{}]  # NOTE: for safety
        import string

        def next_token(index):
            if formula[index] in ['(', ')']:
                return formula[index], index + 1
            if formula[index] in string.ascii_uppercase:
                temp = index + 1
                while temp < len(formula) and formula[temp] in string.ascii_lowercase:
                    temp += 1
                return formula[index: temp], temp

        def next_number(index):
            if index == len(formula):  # NOTE:
                return 1, index

            if formula[index] in string.digits:
                temp = index + 1
                while temp < len(formula) and formula[temp] in string.digits:
                    temp += 1
                return int(formula[index: temp]), temp
            else:
                return 1, index

        def add():
            m = stack.pop(-1)
            if not stack:  # NOTE:
                return m

            last_m = stack.pop(-1)
            key_set = set()
            while last_m:
                [key_set.add(x) for x in m.keys()]
                [key_set.add(x) for x in last_m.keys()]
                for k in key_set:
                    m[k] = m.get(k, 0) + last_m.get(k, 0)
                last_m = stack.pop(-1)
            return m

        index = 0
        while index < len(formula):
            token, index = next_token(index)
            number, index = next_number(index)
            # print(token, number, index)
            if token == '(':
                stack.append({})
            elif token == ')':
                m = add()
                stack.append({k: v * number for k, v in m.items()})
            else:
                stack.append({token: number})

        m = add()
        # NOTE
        return ''.join([str(k) + (str(m[k]) if m[k] > 1 else '') for k in sorted(m.keys())])


formula = "H2O"
print(Solution().countOfAtoms(formula))
