class DebtRecord:
  def __init__(self, b, l, a):
    self.borrower = b
    self.lender = l
    self.amount = a

from collections import defaultdict
from heapq import *
def smallest_debt_record(r):
  # calculate balances
  balances = defaultdict(int)
  for rec in r:
    balances[rec.borrower] -= rec.amount 
    balances[rec.lender] += rec.amount
  
  h = []
  for person in balances.keys():
    heappush(h, (balances[person], person))
  i=0
  res = []
  while i < len(h):
    if res and balances[res[-1]] != balances[h[i][1]]:
      break
    if (h[i][0] < 0):
      res.append(h[i][1])
    else:
      break
    i+=1
  print(h)
  return sorted(res)


s = [
  DebtRecord('Alex', 'Blake', 2),
  DebtRecord('Blake', 'Alex',5),
  DebtRecord('Casey', 'Alex', 5),
  DebtRecord('Blake', 'Casey', 7),
  DebtRecord('Alex', 'Blake', 5),
  DebtRecord('Alex', 'Casey',4 ),
  DebtRecord('Blake', 'Casey', 3),
  DebtRecord('Alex', 'Blake', 1),
  DebtRecord('Alex', 'Casey', 5)
]
print(smallest_debt_record(s))