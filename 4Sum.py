class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        # pruning to reduce run time
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if nums[i] > target/4.0:
                break
            if i > 0 and nums[i] == nums[i-1]: # continue the second time
                continue
            target2 = target - nums[i]
            for j in range(i+1, len(nums)-2):
                if nums[j] > target2/3.0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                target3 = target2 - nums[j]
                # we should use continue not break
                # because target3 changes as j changes
                if nums[k] > target3/2.0:
                    continue
                if nums[l] < target3/2.0:
                    continue
                while k < l:
                    sum_value = nums[k] + nums[l]
                    if sum_value == target3:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        kk = nums[k]
                        k += 1
                        while k<l and nums[k] == kk:
                            k += 1

                        ll = nums[l]
                        l -= 1
                        while k<l and nums[l] == ll:
                            l -= 1
                    elif sum_value < target3:
                        k += 1
                    else:
                        l -= 1
        return result

##        # no count, no in
##        nums.sort()
##        def ksum(num, k, target):
##            i = 0
##            result = set()
##            if k == 2:
##                j = len(num) - 1
##                while i < j:
##                    if num[i] + num[j] == target:
##                        result.add((num[i], num[j])) # set.add((1, 2))
##                        i += 1
##                    elif num[i] + num[j] > target:
##                        j -= 1
##                    else:
##                        i += 1
##            else:
##                while i < len(num) - k + 1:
##                    newtarget = target - num[i]
##                    subresult = ksum(num[i+1:], k - 1, newtarget)
##                    if subresult:
##                        result = result | set( (num[i],) + nr for nr in subresult)
##                        # (1, ) is tuple while (1) is int
##                        # set([(1,2)])|set([(2,3)])
##                    i += 1
##
##            return result
##        return [list(t) for t in ksum(nums, 4, target)]
    
##    def fourSum(self, nums, target):
##        nums.sort()
##        result = []
##        i = 0
##        length = len(nums)
##        while i < length:
##            count = nums.count(nums[i])
##            if count >= 4 and 4*nums[i] == target:
##                result += [[nums[i] for j in range(4)]]
##            if count >= 3 and target - 3*nums[i] in nums[i+count:]:
##                result += [[nums[i] for j in range(3)] + [target - 3*nums[i]]]
##            if count >= 2:
##                result += [[nums[i], nums[i]] + j for j in self.twoSum(nums[i+count:], target - 2*nums[i])]
##            result += [[nums[i]] + j for j in self.threeSum(nums[i+count:], target - nums[i])]
##            i += count
##        return result
##
##    def twoSum(self, nums, target):
##        i = 0
##        j = len(nums)-1
##        result = []
##        while i<j:
##            count_i = nums.count(nums[i])
##            count_j = nums.count(nums[j])
##            if nums[i]+nums[j]<target:
##                i += count_i
##            elif nums[i]+nums[j]>target:
##                j -= count_j
##            else:
##                result += [[nums[i], nums[j]]]
##                i += count_i # duplicated here
##                j -= count_j
##        return result
##
##    def threeSum(self, nums, target):
##        i = 0
##        length = len(nums)
##        result = []
##        while i < length:
##            count = nums.count(nums[i])
##            if count>=3 and 3*nums[i] == target:
##                result += [[nums[i] for j in range(3)]]
##            if count>=2 and target - 2*nums[i] in nums[i+count:]:
##                result += [[nums[i], nums[i], target - 2*nums[i]]]
##            result += [[nums[i]] + j for j in self.twoSum(nums[i+count:], target- nums[i])]
##            i += count
##        return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
nums = [-9,4,0,-3,6,3,-3,-9,-7,1,0,-7,-8,7,1]
target = -9
nums = [-497,-488,-484,-462,-453,-422,-402,-378,-371,-362,
-345,-342,-332,-301,-290,-257,-239,-229,-205,-175,
-98,-92,-90,-87,-73,-67,-63,-61,-40,-37,
-36,-32,-16,-10,0,33,45,53,110,110,
130,147,174,194,207,218,221,247,249,260,
273,278,311,323,335,356,357,371,421,432,
455,482,487]
target = 4941
print(sorted(nums))
print(Solution().fourSum(nums, target))
