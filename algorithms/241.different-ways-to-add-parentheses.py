# -*- coding: cp936 -*-
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        import re, operator
        tokens = re.split('(\D)', input)
        # \D : 2, 3, 4, 5
        # (\D): 2, *, 3, -, 4, *, 5
        # print(tokens)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        # print(nums)
        # print(ops)
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]] # nums
            return [ops[i](a, b) # ops
                    for i in range(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]
        return build(0, len(nums) - 1)
        
##        if not input:
##            return []
##        ans = []
##        # enumerate where the last operation takes place
##        for i in range(len(input)):
##            #print(i, self.diffWaysToCompute(input[:i]), input[i],
##            #      self.diffWaysToCompute(input[i+1:]))
##            if input[i] == '+':
##                ans += [a + b for a in self.diffWaysToCompute(input[:i])
##                        for b in self.diffWaysToCompute(input[i+1:])] # += not =
##            elif input[i] == '-':
##                ans += [a - b for a in self.diffWaysToCompute(input[:i])
##                        for b in self.diffWaysToCompute(input[i+1:])]
##            elif input[i] == '*':
##                ans += [a * b for a in self.diffWaysToCompute(input[:i])
##                        for b in self.diffWaysToCompute(input[i+1:])]
##        return ans if ans else [int(input)] # if no '+-*'

inp = "2-1-1"
inp = "2*3-4*5"
print(Solution().diffWaysToCompute(inp))

'''\A
    Matches only at the start of the string.
\b
    Matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of alphanumeric or underscore characters, so the end of a word is indicated by whitespace or a non-alphanumeric, non-underscore character. Note that formally, \b is defined as the boundary between a \w and a \W character (or vice versa), or between \w and the beginning/end of the string, so the precise set of characters deemed to be alphanumeric depends on the values of the UNICODE and LOCALE flags. For example, r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'. Inside a character range, \b represents the backspace character, for compatibility with Python’s string literals.
\B
    Matches the empty string, but only when it is not at the beginning or end of a word. This means that r'py\B' matches 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'. \B is just the opposite of \b, so is also subject to the settings of LOCALE and UNICODE.
\d
    When the UNICODE flag is not specified, matches any decimal digit; this is equivalent to the set [0-9]. With UNICODE, it will match whatever is classified as a decimal digit in the Unicode character properties database.
\D
    When the UNICODE flag is not specified, matches any non-digit character; this is equivalent to the set [^0-9]. With UNICODE, it will match anything other than character marked as digits in the Unicode character properties database.
\s
    When the UNICODE flag is not specified, it matches any whitespace character, this is equivalent to the set [ \t\n\r\f\v]. The LOCALE flag has no extra effect on matching of the space. If UNICODE is set, this will match the characters [ \t\n\r\f\v] plus whatever is classified as space in the Unicode character properties database.
\S
    When the UNICODE flag is not specified, matches any non-whitespace character; this is equivalent to the set [^ \t\n\r\f\v] The LOCALE flag has no extra effect on non-whitespace match. If UNICODE is set, then any character not marked as space in the Unicode character properties database is matched.
\w
    When the LOCALE and UNICODE flags are not specified, matches any alphanumeric character and the underscore; this is equivalent to the set [a-zA-Z0-9_]. With LOCALE, it will match the set [0-9_] plus whatever characters are defined as alphanumeric for the current locale. If UNICODE is set, this will match the characters [0-9_] plus whatever is classified as alphanumeric in the Unicode character properties database.
\W
    When the LOCALE and UNICODE flags are not specified, matches any non-alphanumeric character; this is equivalent to the set [^a-zA-Z0-9_]. With LOCALE, it will match any character not in the set [0-9_], and not defined as alphanumeric for the current locale. If UNICODE is set, this will match anything other than [0-9_] plus characters classified as not alphanumeric in the Unicode character properties database.
\Z
    Matches only at the end of the string.'''
