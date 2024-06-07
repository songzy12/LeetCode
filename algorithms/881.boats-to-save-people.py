class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        cnt = 0
        people.sort()
        if people[-1] > limit:
            return -1
        tail = len(people) - 1
        head = 0
        while head <= tail:
            if head == tail:
                cnt += 1
                break
            if people[head] + people[tail] <= limit:
                cnt += 1
                head += 1
                tail -= 1
            else:
                cnt += 1
                tail -= 1
        return cnt

people = [3,5,3,4]
limit = 5
print (Solution().numRescueBoats(people, limit))