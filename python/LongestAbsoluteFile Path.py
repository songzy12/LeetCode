# "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"\t\tfile2.ext"
# We are interested in finding the longest (number of characters) absolute path to a file
# Notice that a/aa/aaa/file1.txt is not the longest file path,
# if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            print line
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                # pathlen will get updated regularly
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print Solution().lengthLongestPath(input)

# first thought: dp?
# straight forward as usual
# split by '\n' to get all single dirs or files
# then count the '\t' to get the depth
# if it is a file, update the maxlen
# if it is a dir, update the pathlen
# pathlen will get updated as progress goes on
