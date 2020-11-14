from math import comb
def countTeams(associates, minAssoc, minSkill, maxSkill):
  c = 0
  for a in associates:
    if minSkill <= a <= maxSkill:
      c+=1
  print(c, minAssoc)
  # teams = 0
  # chooseNum = minAssoc
  # while chooseNum <= c:
  #   teams+= comb(c, chooseNum)
  #   chooseNum+=1
  # return teams
  k = minAssoc
  dp = [0 for i in range(k)]
  dp[0] = 1
    
  for i in range(1, c+1):
    for j in range(min(i, k-1), 0, -1):
        dp[j] += dp[j-1]
  print(dp)
  res = 1 << c # 2^n
  for i in range(k):
      res -= dp[i]

  return res



print(countTeams([12, 4, 6, 13, 5, 10], 3, 4, 10))