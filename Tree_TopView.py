""""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

class Queue():
    
    def __init__(self):
        self.items=[]
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
#For sort dictionary
import operator

def topView(root):
    
    if root==None:
        return
    
    my_dict={}
    new_arr=[]
    q1=Queue()
    
    iter_value=0
    #level order traverse
    q1.enqueue(root)
    
    
    my_dict[root]=0
    
    while q1.items!=[]:
        current=q1.dequeue()
        
        #print(current.data)
        
        #print("iter",iter_value)
        
        
        if current.left is not None:
            if current in my_dict:
                if my_dict[current]-1 not in my_dict.values():
                
                    my_dict[current.left]=my_dict[current]-1
            
            q1.enqueue(current.left)
                #my_dict[current.left]=my_dict[current]-1
            
                
            
                
        if current.right is not None:
            if current in my_dict:
                if my_dict[current]+1 not in my_dict.values():
                
                    my_dict[current.right]=my_dict[current]+1
            
                #my_dict[current.right]=my_dict[current]+1
 
                
                
                
            
          
                    
            q1.enqueue(current.right)
        
    #sort dictionary
    my_dict_sorted = sorted(my_dict,key=my_dict.get)
    
    for i in my_dict_sorted:
        print i.data,
   
   # print(my_dict)





        
        
   
    
  #Write your code here
