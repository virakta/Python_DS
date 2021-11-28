'''
   Module Python Datastructures 
   @author Shivakumar Viraktamath
   @email shivmath9@gmail.com
   
   '''

#Linked list
class LList:

    def __init__(self,data=None):
        self.data=data
        self.next=None

    def addToLast(self,data):
        if self.data==None and self.next==None:
              self.data=data
        else:
            tmp=self
            while(tmp.next):
                tmp=tmp.next
            tmp.next=LList(data)  

    def show(self):
        temp=self;
        while(temp.next):
            print(temp.data,end='-->')
            temp=temp.next;
        print(temp.data)

