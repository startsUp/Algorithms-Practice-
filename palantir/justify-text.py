"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

Round robin - space distribution


["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly


1. Collect words till sum(len) > k
2. discard last word
3. Get word count W, number of spaces = max(W - 1, 1) evenly distribute spaces
    spaces to fill = charcount - k
    spaces to fill // number of spaces = distribution 
    remainder = spaces to fill // number of spaces

"""

def justifyLine(words, lineLength):
  wordCount = len(words)
  charLength = sum([len(w) for w in words])
  numSpaces = max(wordCount - 1, 1)
  spacesToFill = lineLength - charLength
  distr = spacesToFill // numSpaces
  remain = spacesToFill % numSpaces
  
  if wordCount == 1:
    return words[0] + ' '*spacesToFill
  
  res = ''
  for i in range(len(words) - 1):
    w = words[i]
    res += w
    res += ' '*distr
    if remain != 0:
      res+= ' '
      remain -= 1
  return res + words[-1]

def justifyText(text, lineLength):
  start = 0
  curLength = 0
  lines = []
  for i, word in enumerate(text):
    if curLength + len(word) > lineLength:
      lines.append(justifyLine(text[start:i], lineLength))
      start = i
      curLength = len(word) + 1
    else:
      curLength+= len(word) + 1
  lines.append(justifyLine(text[start:], lineLength))
  return lines

test = ["the", "omatsadkaposkd"] 
k = 16
print(justifyText(test, k))
    

