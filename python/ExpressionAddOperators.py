class Solution(object):
    def __init__(self):
        self.ans = []
        self.num = 0
        self.target = 0
        
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.num = num
        self.target = target
        if not num:
            return []
        self.addOperatorsHelper('', 0, 0, 0)
        return self.ans
    
    def addOperatorsHelper(self, path, pos, val, multed):
        if pos == len(self.num) and self.target == val:
            self.ans += path,
            return
        for i in range(pos, len(self.num)):
            # cur will starts with 0 
            if i != pos and self.num[pos] == '0':
                break
            cur = self.num[pos:i+1]
            if pos == 0:
                self.addOperatorsHelper(cur, i+1, int(cur), int(cur))
            else:
                self.addOperatorsHelper(path+'+'+cur, i+1, val+int(cur), int(cur))
                self.addOperatorsHelper(path+'-'+cur, i+1, val-int(cur), -int(cur))
                # val - multed + multed*int(cur)
                self.addOperatorsHelper(path+'*'+cur, i+1, val-multed+multed*int(cur), multed*int(cur))

num, target = '00', 0
print Solution().addOperators(num, target)
