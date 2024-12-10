class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=node(data)
        if(self.root==None):
            self.root=newnode
            return
        temp=self.root
        while True:
            if data < temp.data:
                if temp.left==None:
                    temp.left=newnode
                    break
                else:
                    temp=temp.left

            if data > temp.data:
                if temp.right==None:
                    temp.right=newnode
                    break
                else:
                    temp=temp.right
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

tree=bst()

n=int(input())
for i in range(n):
    c=int(input())
    tree.insert(c)

tree.inorder(tree.root)

