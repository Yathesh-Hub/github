arr=[]
ver=int(input())
edge=int(input())
for i in range(ver):
    arr.append([0 for i in range(ver)])
for i in range(edge):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1
for i in range(ver):
    for j in range(ver):
        print(arr[i][j],end=" ")
    print(" ")
