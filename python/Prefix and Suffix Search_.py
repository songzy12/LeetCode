class WordFilter(object):

    def __init__(self, words):
        from collections import defaultdict
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.weights = {}
        for index, word in enumerate(words):
            prefix, suffix = '', ''
            for char in [''] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [''] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = index

    def f(self, prefix, suffix):
        weight = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight

##class WordFilter(object):
##
##    def __init__(self, words):
##        self.inputs = {}
##        for index, word in enumerate(words):
##            prefix = ''
##            for char in [''] + list(word):
##                prefix += char
##                suffix = ''
##                for char in [''] + list(word[::-1]):
##                    suffix += char
##                    self.inputs[prefix + '.' + suffix[::-1]] = index
##
##    def f(self, prefix, suffix):
##        return self.inputs.get(prefix + '.' + suffix, -1)
