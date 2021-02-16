## Chapter 6, exercise 5 Algorithms Design
wordDict = ['meet', 'at', 'eight']
def quality(x):
  if x in wordDict:
    return 10
  else:
    return -1


"""
  meetateight
  quality('m')
  quality('me')

"""
def highestQualitySegmentation(y):
  dp = [(float('-inf'),0) for _ in range(len(y) + 1)]
  dp[0] = (0, 0)
  for i in range(1,len(y)+1):
    segment = ''
    for j in range(i, -1, -1):
      segment= y[j-1] + segment
      qual = quality(segment)
      if qual + dp[j-1][0] > dp[i][0]:
        dp[i] = (qual + dp[j-1][0], j)  
	
	# collect segments
  print(dp)
  i = len(y)
  segments = []
  while i > 0:
    print(segments, i)
    segments.append(y[dp[i][1]-1: i])
    i = dp[i][1]-1
	
  return segments
word = 'meetateight'
print(highestQualitySegmentation(word))