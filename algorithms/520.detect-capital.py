class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if all([c.isupper() for c in word]):
            return True
        if all([not c.isupper() for c in word]):
            return True
        return word[0].isupper() and all([not c.isupper() for c in word[1:]])
