class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        def backtrack(start_idx, curr_arr):
           
            if start_idx == n:
                res.append(curr_arr[:])
                return
            
            for i in range(start_idx, n):
                sub_string = s[start_idx:i+1]
                if sub_string == sub_string[::-1]:
                    curr_arr.append(sub_string)
                    backtrack(i + 1, curr_arr)  
                    curr_arr.pop()

        backtrack(0, [])
        return res
            

       






            

            

        