class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False
            
        used = [False] * len(nums)
        
        def backtrack(i, count, current_sum):
           
            if count == k - 1:
                return True
            
            
            if current_sum == target:
                return backtrack(0, count + 1, 0)
            
            for j in range(i, len(nums)):
                
                if used[j] or current_sum + nums[j] > target:
                    continue
                
                
                if j > 0 and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue
                
                used[j] = True
                if backtrack(j + 1, count, current_sum + nums[j]):
                    return True
                used[j] = False
                
            return False

        return backtrack(0, 0, 0)