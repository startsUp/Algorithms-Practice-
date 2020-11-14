def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [float('inf')] * n
        dp2 = [0] * n

        for day in range(d):
            stack = []
            for x in range(day, n):
                if x:
                    dp2[x] = dp[x - 1] + jobDifficulty[x]
                else:
                    dp2[x] = jobDifficulty[x]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[x]:
                    job = stack.pop()
                    dp2[x] = min(dp2[x], dp2[job] - jobDifficulty[job] + jobDifficulty[x])
                if stack:
                    dp2[x] = min(dp2[x], dp2[stack[-1]])
                stack.append(x)
            dp = dp2
            dp2 = [0] * n

        return dp[-1]