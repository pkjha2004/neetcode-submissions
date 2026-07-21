class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n =  len(matchsticks)
        s = sum(matchsticks) // 4
        if sum(matchsticks) % 4 != 0:
            return False
        sides = [0]*4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > s:
            return False

        def backtrack(index: int) -> bool:

            if index == n:
                return True

            for i in range(4):
                if sides[i] + matchsticks[index] <= s:
                    sides[i] = sides[i] + matchsticks[index]

                    if backtrack(index+1):
                        return True
                    sides[i]-= matchsticks[index]
                    if sides[i] == 0:
                        break
                
            return False
        return backtrack(0)

                    







                


                    




              

                
        