class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None

    


def printout(head):
    while(head!=None):
        print(head.data)
        head=head.next


def insert_end(head,data):
    iter_1=head

    if head==None:
        n_node=Node(data,None)

        return n_node
       
    

        

    else:
        while (iter_1.next!=None):
            iter_1=iter_1.next

        n_node=Node(data,None)

        iter_1.next=n_node

    return head




head=None

head=insert_end(head,5541)
head=insert_end(head,1552)
head=insert_end(head,1553)
head=insert_end(head,134)


printout(head)