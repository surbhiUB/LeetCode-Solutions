def numRollsToTarget(self,dice,faces,target):
    memo = {}

    def rolls(dice,target):
        if target>dice*faces:
            memo[dice,target] = 0
            return 0
        if dice==0: 
            return 0 if target >0 else 1
        if target<0:
            return 0
        
        if(dice,target) in memo:
            return memo[dice,target]

        ways = 0
        for num in range(1,f+1):
            ways+= rolls(dice-1,target-num)
        memo[dice,target] = ways
        return ways
    return rolls(dice,target)%(10**9+7)
