class queue:
    def __init__(self):
        self.arr=[]
    def enqueue(self,data):
        return self.arr.append(data)
    def dequeue(self):
        return self.arr.pop(0)
    def peek(self):
        return self.arr[0]
    def display(self):
        return self.arr


o=queue()
while True:
    c=int(input())
    if c==1:
        v=int(input())
        o.enqueue(v)
    elif c==2:
        print(o.dequeue())
    elif c==3:
        print(o.peek())
    elif c==4:
        print(o.display())
    elif c==5:
        print("Exit")
        break
    else:
        print("Invalid")