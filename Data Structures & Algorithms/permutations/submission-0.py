class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        visited = set()
        def backtrack(curr_arr ):
            if len(curr_arr) == n:
                res.append(curr_arr[:])
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    curr_arr.append(num)
                    backtrack(curr_arr)
                    curr_arr.pop()
                    visited.remove(num)

        backtrack([])
        return res
            
        