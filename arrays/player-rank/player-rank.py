def Solution():
  def playerRankUp(self, scores, cutOff):
    scores.sort(reversed=True)
    curRank = 1
    prevScore = -1
    i=0
    while curRank <= cutOff:
      curScore = scores[i]
      if (prevScore != curScore):
        curRank+=1
      i+=1
    return ans
    

