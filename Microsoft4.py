#problem 462 of LC
class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        n = len(nums)

        #find median
        x = 0
        if n%2 == 0:
            x = (nums[n//2 -1] + nums[n//2]) / 2
        else:
            x = nums[n//2]


        median = x
        moves = 0
        for i in nums:
            moves += abs(i - median)
        return moves

