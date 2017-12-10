class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        def build_targets(target):
            import string
            letters = string.ascii_lowercase
            index = letters.find(target)
            return letters[index+1:] + letters[:index]
        targets = build_targets(target)
        letters = set(letters)
        for target in targets:
            if target in letters:
                return target

        return ''

letters = ['c', 'f', 'j']
target = 'k'
print(Solution().nextGreatestLetter(letters, target))
