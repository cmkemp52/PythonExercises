lis = [5,2,1,7,3,8,9,-40,5,20,80,-23, 2, 5, 7]

sm=0
for num in lis:
    sm+=num
print(sm)

print("")
print(max(lis))

print("")
print(min(lis))

print("")
print("EVEN")
for num in lis:
    if(num%2==0):
        print(num)

print("")
print("POSITIVE")
for num in lis:
    if(num>0):
        print(num)

print("")
print("LIST POSITIVE")
lis2 = []
for num in lis:
    if(num>0):
        lis2.append(num)
print(lis2)

print("")
print("MULTIPLY LIST")
mul = int(input("Please give a number: "))
newlis = []
for num in lis:
    newlis.append(num*mul)
print(newlis)

print("")
print("MULTIPLY VECTORS")
lis1 = [2,4,5]
lis2 = [2,3,6]
i=0
anser= []
while(i < len(lis1)):
    anser.append(lis1[i]*lis2[i])
    i+=1
print(anser)

print("")
print("Matrix Addition (Scaling)")
matr1 = [[1,3],[2,4]]
matr2 = [[5,2],[1,0]]

i = 0

results = [[0]*len(matr1) for i in range(len(matr1))]

while(i<len(matr1)):
    x=0
    while(x<len(matr1)):
        results[i][x] = (matr1[i][x]+matr2[i][x])
        x+=1
    i+=1

print(results)

print("")
print("DE-DUP")
nodup = []

i=0

for num in lis:
    for dup in nodup:
        if(num!=dup):
            i+=1
    if(i==len(nodup)):
        nodup.append(num)
    i=0

print(nodup)


print("")
print("MATRIX MULTIPLICATION")

matrix1=[[2,-2],[5,3]]
matrix2=[[-1,4],[7,-6]]

resl=[[0,0],[0,0]]

resl[0][0] = matrix1[0][0]*matrix2[0][0]+matrix1[1][0]*matrix2[0][1]
resl[1][0] = matrix1[0][0]*matrix2[1][0]+matrix1[1][0]*matrix2[1][1]
resl[0][1] = matrix1[0][1]*matrix2[0][0]+matrix1[1][1]*matrix2[0][1]
resl[1][1] = matrix1[0][1]*matrix2[1][0]+matrix1[1][1]*matrix2[1][1]

print(resl)