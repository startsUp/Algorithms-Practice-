import string
def preprocess(word):
  result = ""
  for c in word:
    if c not in string.punctuation:
      result += c.lower()
  return result

def topKMostFrequentKeyWords(k,keywords,reviews):

  count = {} # Map keywords to the number of times they occur
  
  kw = set([w.lower() for w in keywords]) # Store keywords in a set (make sure they are lowercase)

  # Iterate through each review
  for review in reviews:
    seen = set() # Use a set to make sure we count each keyword only once per review
    words = review.split(" ") # Split review into words
    # Iterate through each word in the review
    for word in words:
      w = preprocess(word) # Preprocess the word to convert to lower case, and strip punctuation
      if w in kw and w not in seen:
        count[w] = count.get(w,0) + 1
        seen.add(w)

  # Sort key,value pairs descending order of frequency, ascending order of lexicographical
  sortedFrequencies = sorted(count.items(),key=lambda x: (-x[1],x[0]) )

  # Return just top k keywords
  return [x[0] for x in sortedFrequencies[:k]]