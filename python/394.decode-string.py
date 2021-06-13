# Given an encoded string, return it's decoded string.
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s

# first thought: use a finite state machine
# use powerful tool: regular expression 
