# faster method

# import java.util.*;
# import java.io.*;
# import java.lang.*;

# //If no other cities share an x or y coordinate, return null
# public class Solution {
#     public String[] findNearestCities(int numOfCities,String[] cities, int[] xCoordinates,int[] yCoordinates,int numOfQueries,
#                                  String[] queries) {
                                     
#         HashMap<String,Map.Entry<String,Integer>> map = new HashMap<>();
#         PriorityQueue<Map.Entry<String,Integer>> pq[] = new PriorityQueue[numOfCities];
#         HashMap<String,Integer> map1 = new HashMap<>();
#         for(int i = 0;i<cities.length;i++){
#             map1.put(cities[i],i);
#         }
#         for(int i = 0;i<pq.length;i++)
#             pq[i] = new PriorityQueue<>((a,b) -> a.getValue()-b.getValue()!=0?a.getValue()-b.getValue():a.getKey().compareTo(b.getKey()));
#         for(int i = 0;i<xCoordinates.length;i++){
#             for(int j = 0;j<xCoordinates.length;j++){
#                 if(i == j)
#                     continue;
#                 if(xCoordinates[i] == xCoordinates[j]){
#                     int x = Math.abs(xCoordinates[i] - xCoordinates[j]);
#                     int y = Math.abs(yCoordinates[i] - yCoordinates[j]);
#                     int d = x+y;
#                     HashMap<String,Integer> m = new HashMap<>();
#                     m.put(cities[j],d);
#                     for(Map.Entry<String,Integer> e : m.entrySet())
#                         pq[i].offer(e);
#                 }
#             }
#         }
#         for(int i = 0;i<yCoordinates.length;i++){
#             for(int j = 0;j<yCoordinates.length;j++){
#                 if(i == j)
#                     continue;
#                 if(yCoordinates[i] == yCoordinates[j]){
#                     int x = Math.abs(xCoordinates[i] - xCoordinates[j]);
#                     int y = Math.abs(yCoordinates[i] - yCoordinates[j]);
#                     int d = x+y;
#                     HashMap<String,Integer> m = new HashMap<>();
#                     m.put(cities[j],d);
#                     for(Map.Entry<String,Integer> e : m.entrySet())
#                         pq[i].offer(e);
#                 }
#             }
#         }
#         String res[] = new String[numOfQueries];
#         for(int i = 0;i<queries.length;i++){
#             int idx = map1.get(queries[i]);
#             if(!pq[idx].isEmpty()){
#                 Map.Entry<String,Integer> e = pq[idx].peek();
#                 res[i] = e.getKey();
#             }
#             else res[i]= null;
#         }
#         return res;                            
#     }
# }





"""
#If no cities found, return None instread of string "None" 
def findNearestCities(numOfCities: int, cities: List[str], x: List[int], y: List[int],
                      numOfQueries: int, queries: List[str]) -> List[str]:
    result = []
    for city in queries:
        temp = getNeighbours(city, x, y)
        if len(temp) == 1:
            result.append(cities[temp[0]])
        elif len(temp) == 0:
            result.append(None)
        else:
            cityList = []
            for ele in temp:
                cityList.append(cities[ele])
            result.append(sorted(cityList)[0])
    return result
                
def getNeighbours(queryCity, xCoordinates, yCoordinates):
    finalList = []
    minDist = float('inf')

    ind = cities.index(queryCity)
    x = xCoordinates[ind]
    y = yCoordinates[ind]

    for i in range(0, numOfCities):
        if i != ind and (xCoordinates[i] == x or yCoordinates[i] == y) :
            distance = getDistance(x, y, xCoordinates[i], yCoordinates[i])
            if distance < minDist:
                finalList = []
                minDist = distance
                finalList.append(i)
            elif distance == minDist:
                finalList.append(i)
    return finalList
    
def getDistance(x1,y1,x2,y2):
    distance = abs(x1-x2)+abs(y1-y2)
    return distance
    """