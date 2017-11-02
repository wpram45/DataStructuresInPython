class Node:

    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key


def search(root,value):
    while root != None:
        if(value==root.val):
            return "bulundu"
        elif (value < root.val):
            root=root.left
        else:
            root=root.right


    return
def min(root):
    while(root.left.left!=None):
        root=root.left

    print("Atası",root.val,"Kardesi :",root.right.val)


def max(root):
    while(root.right.right!=None):
        root=root.right
    print("Atası",root.val,"Kardesi :",root.left.val)

def insert(root,node):
    if root is None:
        root=node

    else:
        if root.val < node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node

            else:
                insert(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

inorder(r)
print(search(r,80))
min(r)
max(r)
