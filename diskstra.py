class graph:
    def __init__(self,val):
        self.ver=val
        self.graph=[[0 for i in range(val)]for i in range (val)]
    def addedge(self,u,v,w):
        self.graph[u][v]=w
        self.graph[v][u]=w
    def min_distance(self,d,b):
        a=float("inf")
        a_ind = -1
        for i in range(self.ver):
            if d[i]<a not in b[i]:
                a=d[i]
                a_ind=i
        return a
    def dijkstra(self,src):
        d=float[("inf")]*self.ver
        d[src]=0
        b=[False]*self.ver
        for i in range(self.ver):
            u=self.min_distance(d,b)
            b[u]=True
            for v in range(self.ver):
                if self.graph[u][v]>0 and not b[v] and d[u]+self.graph[u][v]<d[v]:
                    d[v]=d[u]+self.graph[u][v]
        return d

n=int(input())
Graph=graph()
for i in range(n):
    u,v,w=map(int,input().split())
    Graph.addedge(u,v,w)
src=int(input())
res=Graph.dijkstra(src)
print(res[i])