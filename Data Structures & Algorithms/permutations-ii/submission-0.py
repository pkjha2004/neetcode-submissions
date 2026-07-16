class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def backtrack(curr_arr, visited):
            if len(curr_arr) == n :
                res.append(curr_arr[:])
                return
            for i in range(n):
                if i in visited:
                    continue  
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited :
                    continue
                
                visited.add(i)
                curr_arr.append(nums[i])
                backtrack(curr_arr, visited)
                visited.remove(i)
                curr_arr.pop()

        backtrack([], set())
        return res

        