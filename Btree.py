class node:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None
class binarytree:
    def __init__(self,data):
        self.root=node(data)
    def insert(self,data):
        newnode=node(data)
        if(self.root==None):
            self.root=newnode
            return
        queue=[self.root]
        while queue:
            temp=queue.pop(0)
            if temp.left==None:
                temp.left=newnode
                break
            else:
                queue.append(temp.left)
            if temp.right==None:
                temp.right=newnode
                break
            else:
                queue.append(temp.right)
    def display(self,node):
        if node:
            self.display(node.left)
            print(node.data)
            self.display(node.right)

n=int(input())
tree=binarytree(n)
m=int(input())
for i in range(m):
    s=int(input())
    tree.insert(s)
tree.display(tree.root)
