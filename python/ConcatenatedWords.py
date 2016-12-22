class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        S = set(words)
        ans = []
        for word in words:
            if not word: continue
            stack = [0]
            seen = {0}
            M = len(word)
            while stack:
                node = stack.pop()
                if node == M:
                    ans.append(word)
                    break
                for j in xrange(M - node + 1):
                # use a set since `in` is fast
                    if (word[node:node+j] in S and
                        node + j not in seen and
                        (node > 0 or node + j != M)):
                        stack.append(node + j)
                        seen.add(node + j)

        return ans

# for each i, chech each j > i, whether word[i:j] in words
# another way: for each j, check each i < j, whether word[i:j] in words
