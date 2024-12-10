class queue:
    def __init__(self):
        self.arr=[]
    def enrear(self,val):
        return self.arr.append(val)
    def derear(self):
        return self.arr.pop()
    def enfront(self,val):
        return self.arr.insert(val)
    def defront(self):
        return self.arr.pop(0)
    def rearpeek(self):
        return self.arr[-1]
    def frontpeek(self):
        return self.arr[0]
    def display(self):
        print(self.arr)
    
r=queue()

while True:
    ch=int(input())
    if(ch==1):
        s=int(input())
        r.enrear(s)
    elif(ch==2):
        s=int(input())
        r.derear(s)
    elif (ch==3):
        s=int(input())
        r.enfront(s)
    elif(ch==4):
        e=r.defront()
        print(e)
    elif(ch==5):
        e=r.rearpeek()
        print(e)
    elif (ch==6):
        e=r.frontpeek()
        print(e)
    elif(ch==7):
        r.display()
    elif(ch==8):
        print("Exit")
        break
    else:
        print("Invalid")