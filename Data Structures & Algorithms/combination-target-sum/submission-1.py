class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len((candidates))
        res = []
        def backtrack(i,curr_sum, curr_arr ):
            if curr_sum > target or i == n:
                return
            if curr_sum == target:
                res.append(curr_arr)
                return
            include = backtrack(i, curr_sum + candidates[i], curr_arr + [candidates[i]])
            exclude = backtrack(i+1, curr_sum,curr_arr)
        backtrack(0, 0, [])
        return res
        