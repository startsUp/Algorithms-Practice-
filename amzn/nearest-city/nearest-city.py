def solve(numOfCities, cities, x, y, numOfQueries, queries):
  shared_x = {}
  shared_y = {}
  city_map = {}
  for i in range(numOfCities):
    city_map[cities[i]] = i
    if x[i] in shared_x:
      shared_x[x[i]].append(i)
    else:
      shared_x[x[i]] = [i]
    
    if y[i] in shared_y:
      shared_y[y[i]].append(i)
    else:
      shared_y[y[i]] = [i]
  sol = []
  for j in range(numOfQueries):
    idx = None
    query = queries[j]
    i = city_map[query]
    m = 999
    if x[i] in shared_x:
      for city in shared_x[x[i]]:
        if city != i and abs(x[city] - x[i])+abs(y[city] - y[i]) < m:
          idx = city
          m =abs(x[city] - x[i])+abs(y[city] - y[i])
    if y[i] in shared_y:
      for city in shared_y[y[i]]:
        if city != i and abs(x[city] - x[i])+abs(y[city] - y[i]) < m:
          idx = city
          m = abs(x[city] - x[i]) + abs(y[city] - y[i])
    if idx == None:
      sol.append(None)
    else:
      sol.append(cities[idx])
    
  return sol