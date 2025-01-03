#problem 1248 of LC

#Count number of Nice Subarrays

#TC : O(n^3) TLE
class Solution(object):
    def numberOfSubarrays(self, nums, k):

        def subarrays(arr, k):
            n = len(arr)
            result = []
            for i in range(n):
                for j in range(i+1, n+1):
                    tempArray = arr[i:j]
                    if len(tempArray) >=k and Findodds(tempArray) == k:
                        result.append(tempArray)
            return result
        
        def Findodds(nums):
            temp = 0
            for i in nums:
                if i%2 != 0:
                    temp +=1
            return temp
        
        return len(subarrays(nums, k))

        
