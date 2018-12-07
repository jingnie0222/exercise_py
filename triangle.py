#!/usr/bin/python

row = 10
#triangle = [[1],[1,1]]  row 1,2 is special case
triangle = [[1]]   #row 1 is special case, the programm can generate the row 2

for i in range(1,row):
    pre = triangle[i-1]
    cur = [1]
    for j in range(0,i-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)

print(triangle)

