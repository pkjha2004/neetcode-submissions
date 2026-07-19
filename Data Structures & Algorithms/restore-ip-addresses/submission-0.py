class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []                  
        def backtrack(start_idx,dots, curr_str):
            #conditional statement
            if dots == 4 and start_idx == n:
                res.append(curr_str[:-1]) # to remove the last dot
                return
            if dots > 4:
                return
            for i in range(start_idx, min(start_idx +3, n)):
                sub_str = s[start_idx:i+1]
                if start_idx != i and s[start_idx] == '0':# identifying if there is a trailing 0
                    continue
                if int(sub_str) < 256:
                    backtrack(i+1, dots +1, curr_str + sub_str +"." )
        backtrack(0, 0, "")
        return res

                

            