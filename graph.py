class node:
    def init(self,data):
        self.data=data
        self.next=None
class graph:
    def init(self,n):
        self.arr={i:None for i in range(n)}
    def create(self,a,b):
        newnode=node(a)
        newnode.next=self.arr[b]
        self.arr[b]=newnode
        newnode=node(b)
        newnode.next=self.arr[a]
        self.arr[a]=newnode
    def display(self):
        for i in self.arr:
            print(i)
            temp=self.arr[i]
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print("")
var=int(input())
edge=int(input())
Graph=graph(var)
for i in range(edge):
    a,b=map(int,input().split())
    Graph.create(a,b)
Graph.display()