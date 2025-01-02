#problem 2970 of LC

# Count number of Incremovable Subarrays - I
class Solution(object):
    def incremovableSubarrayCount(self, nums):
        def StrictlyIncrease(array):
            flag = True
            for i in range(1, len(array)):
                if array[i] <= array[i-1]:
                    flag = False
            return flag
        c=0
        def CanRemove(nums, start, end):
            if start ==0:
                return StrictlyIncrease(nums[end:])
            if end == len(nums):
                return StrictlyIncrease(nums[:start])
            return StrictlyIncrease(nums[:start] +nums[end:])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if CanRemove(nums, i, j):
                    c +=1
        return c