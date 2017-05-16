class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        temp = []
        for i, t in enumerate(n[::-1]):
            if not temp:
                temp.append(t)
                continue
            if t >= temp[-1]:
                temp.append(t)
                continue
            tail = []
            while t >= temp[0]:
                tail.append(temp.pop(0))
            mid = temp[0]
            tail.append(t)
            temp.pop(0)
            while temp:
                tail.append(temp.pop(0))

            ans = int(n[:len(n)-i-1] + mid + ''.join(tail))
            return ans if ans <= (1<<31-1) else -1
        return -1

if __name__ == '__main__':
    n = 12354
    print Solution().nextGreaterElement(n)
