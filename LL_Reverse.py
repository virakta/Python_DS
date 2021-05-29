'''
   Module Python Datastructures 
   @author Shivakumar Viraktamath
   @email shivmath9@gmail.com
   
   '''
from Python_DS import LList
#Reverseing a linked list

def reverse_a_linked_list(ll):
    prvnode=None
    currnode=ll
    while(currnode != None):
        nextnode=currnode.next
        currnode.next=prvnode
        prvnode=currnode
        currnode=nextnode
    return prvnode




ll= LList('a')
ll.addToLast('b')
ll.addToLast('c')
ll.addToLast('d')
ll.addToLast('e')
ll.addToLast('f')
ll.addToLast('g')

ll.show()

ll_reversed= reverse_a_linked_list(ll)
print("Reversed List")
ll_reversed.show()