class Node(object):
    def __init__(self, c):
        self.c = c
        self.last = None
        self.next = None
    
class Solution(object):
    def convert(self, senate):
        head = Node(senate[0])
        cur = head
        for i in range(1, len(senate)):
            temp = Node(senate[i])
            cur.next = temp
            temp.last = cur
            cur = temp
        cur.next = head
        head.last = cur
        return head

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        numR = senate.count('R')
        numD = senate.count('D')
        bannedR = 0
        bannedD = 0
        storeR = 0
        storeD = 0

        head = self.convert(senate)
        cur = head
        while bannedR < numR and bannedD < numD:
            if head.c == 'D':
                if storeD > 0:
                    
                    head.last.next = head.next
                    head.next.last = head.last
                    storeD -= 1
                else:
                    bannedR += 1
                    storeR += 1
            else:
                if storeR > 0:
                    head.last.next = head.next
                    head.next.last = head.last # remember this
                    storeR -= 1
                else:
                    bannedD += 1
                    storeD += 1
            # print numR, numD, head.c, bannedR, bannedD, storeR, storeD
            head=head.next

        if bannedR == numR:
            return 'Dire'
        return 'Radiant'

print Solution().predictPartyVictory("RRDRDDRDRRDDDDDRDRDR")

# "Radiant"
