from collections import Counter
def max_profit(inv, units_ordered):
  c = Counter(inv)
  profit = 0
  maxStock, minStock = max(inv), min(inv)
  cur_units = 0
  unfullfilled = units_ordered
  while maxStock >= 0 and unfullfilled > 0:
    cur_units+= c[maxStock] if maxStock in c else 0
    print('Stock of ', maxStock, ' with units ', cur_units)
    units = min(unfullfilled, cur_units)
    unfullfilled -= units
    profit += units*maxStock
    maxStock-=1
  return profit

print(max_profit([2, 8, 4, 10, 6], 20))
    
