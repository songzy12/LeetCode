class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        n = len(s)
        ans = 0
        st = []
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                if len(st):
                    if s[st[-1]] == '(':
                        st.pop(-1)
                    else:
                        st.append(i)
                else:
                    st.append(i)
        if not len(st):
            return n
        a, b = n, 0
        while len(st):
            b = st.pop(-1)
            ans = max(ans, a-b-1)
            # substring between adjacent indices should be valid parentheses
            a = b
        ans = max(ans, a)
        return ans

s = '(()'
s = ')()()('
s = '(()(()(()'
print(Solution().longestValidParentheses(s))
