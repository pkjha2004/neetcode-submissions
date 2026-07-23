class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        count = 0
        def backtrack(index, curr_sum):
            nonlocal count
            if index == n and curr_sum == target :
                count+=1
                return                     
            if  index == n and curr_sum != target:
                return 
            sum1 = curr_sum + nums[index]
            backtrack(index+1, sum1)
            sum2 = curr_sum - nums[index]
            backtrack(index+1, sum2)
        backtrack(0, 0)
        return count




        