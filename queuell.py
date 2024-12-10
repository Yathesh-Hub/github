class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        if(self.front==None):
            self.rear=node(data)
            self.front=self.rear
        else:
            newnode=node(data)
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        self.front=self.front.next
    def peek(self):
        print(self.front.data,self.front.next)
    def display(self,data):
        temp=self.data
        while(temp!=None):
            print(temp.data,id(temp.data))
            temp=temp.next

o=queue()
n=int(input())
for i in range(n):
    m=int(input())
    o.enqueue(m)
o.display()
o.dequeue()
o.display()
o.peek()
