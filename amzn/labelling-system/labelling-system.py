import heapq
originalLabel = "baccc"
charLimit = 2

label_list = [-1*ord(char) for char in originalLabel]
heapq.heapify(label_list)

final_label = ""
tmp_lst = []

while len(label_list) > 0:
  item = heapq.heappop(label_list)
  value = chr(item *-1)

  if len(final_label) >= charLimit:
    n = len(final_label)
    substring = final_label[n-charLimit:n+1]
    if (substring == (value * charLimit)):
      tmp_lst.append(item)
    else:
      final_label += value
      for val in tmp_lst:
        heapq.heappush(label_list,val)
      tmp_lst = []
  else:
    final_label += value

print(final_label)