def rotate(matrix):

    n = len(matrix) - 1

    while(n>=1):

        x, y = n, len(matrix) - 1 - n # n = 3

        r, c = x, y
       # print('r', 'c', r, c)
        while(r >= 0 and c >= 0 and r <= x and c < len(matrix) - 1 - y):

            i, j = r, c
          #  print('i', 'j', i, j)
            while True:

                sI, sJ = len(matrix) -1 - j, i
                #print('si', 'sj', sI, sJ, y, c)
                matrix[i][j], matrix[sI][sJ] = matrix[sI][sJ], matrix[i][j]

                if sJ == y and sI != r:
                    break
                
                i = sI
                j = sJ

            c += 1

        n-=1

   

 

def printL(matrix):

    for i in matrix:

        print(i)

x = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]

y = [[13, 14, 15, 16], [9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]]

printL(x)

rotate(x)
print('---- rotated ---- ')
printL(x)