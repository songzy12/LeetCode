class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        # the sort() function and the index() function are too slow.
        # use dict will shorten the time of searching index
        # care for {3,2,4},6 and {0,1,2,0},0
        d={}
        # use xrange() not range() as much as possible
        for i in range(len(num)):
            # examine for the element in dictionary
            
# can not make dict of different values for same key
            if target-num[i] in d:
                return d[target-num[i]]+1,i+1
            # if answer has not shown up, add the element into dict
            else:
                d[num[i]]=i
            
        
##        # reverse num to avoid (3,2,4),6
##        # in fact I am imitating the rindex() 
##        temp=[ x for x in num]
##        temp.reverse()
##        #exam one by one
##        for i in num:
##            # to see whether num contains target-i 
##            if (target-i in num \
##               # and the index search from start and from end are not same
##               and num.index(i)+temp.index(target-i)!=len(num)-1):
##                return (num.index(i)+1,len(num)-temp.index(target-i))
            
##        # be careful to use deep copy
##        temp=[x for x in num]
##        # sort num for convinence
##        temp.sort()
##        # record the original index
##        index=[num.index(i) for i in temp]
##        # use a O(n) algorithm
##        i=0
##        j=len(num)-1
##        while i<j:
##            if temp[i]+temp[j] < target:
##                i+=1
##            elif temp[i]+temp[j] > target:
##                j-=1
##            else:
##                break
##        return (index[i]+1,index[j]+1)

num=[3,2,4]
target=6
print (Solution().twoSum(num,target))
