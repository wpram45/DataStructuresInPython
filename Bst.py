class BinarySearchTree:
    veri=None
    sag=None
    sol=None



def ekle(root,veri):
    head=root
    if root is None:
        root=BinarySearchTree()
        root.veri=veri
        root.sag=None
        root.sol=None

        return root
    if root.veri < veri:
        if root.sag is None:
            root.sag=BinarySearchTree()
            root.sag.veri=veri
            root.sag.sag=None
            root.sag.sol=None

            

        else:
            ekle(root.sag,veri)
    else:
        if  root.sol is None:
            root.sol=BinarySearchTree()
            root.sol.veri=veri
            root.sol.sol=None
            root.sol.sag=None
            
        
        else:
            ekle(root.sol,veri)
    return head


def inorder(root):

    
    if root is not None:
        inorder(root.sol)
        print(root.veri)
        inorder(root.sag)
        

root=None
root=ekle(root,30)
root=ekle(root,20)
root=ekle(root,40)
root=ekle(root,70)
root=ekle(root,60)
root=ekle(root,80)
root=ekle(root,50)

inorder(root)
