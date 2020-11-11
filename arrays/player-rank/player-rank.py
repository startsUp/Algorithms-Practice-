"""
  Players playing a game where they have a cutoff rank to level up their character. 
  Given scores of at the end of round how many players will be able to level up their 
  character?

  Players with equal scores will have equal ranks, but the player with
  the next lowest score will be ranked based on the position within the list of all players'
  scorres. 
  for example, if there are four players, and three players tie for first place,
  their ranks would be 1, 1, 1 and 4. also, no player with score of 0 can level up, no
  matter their rank.

  Determine count of players able to level up their rank

"""

def player_rank(scores, cutOffRank):
  counts = [0 for i in range(101)]
  for score in scores:
    counts[score]+=1

  rank = 0
  for i in range(100, -1, -1):
    rank+=counts[i]
    if (cutOffRank <= rank):
      break
  
  return rank

print(player_rank([25,25,25,50,100], 2))

