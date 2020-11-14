from math import comb
def countTeams(associates, minAssoc, minSkill, maxSkill):
  c = 0
  for a in associates:
    if minSkill <= a <= maxSkill:
      c+=1
  print(c, minAssoc)
  
  # once we know the associates that fall within the threshold, its only a matter or choosing the team composition and number of members
  # we start with a team size of min Associates all the way up to countAssociates 
  # for each time size use n choose k combinations to get the number of unique teams (without ordering) we can form with given team members
  # to optimize run time, we can use a dynamic approach to find nC0 + nC1 .... + nC(k-1) = 2^n - (nCk + nC(k+1) + ... nCn)

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


  # teams = 0
  # chooseNum = minAssoc
  # while chooseNum <= c:
  #   teams+= comb(c, chooseNum)
  #   chooseNum+=1
  # return teams

print(countTeams([12, 4, 6, 13, 5, 10], 3, 4, 10))