'''
   Module Python Datastructures 
   @author Shivakumar Viraktamath
   @email shivmath9@gmail.com
   
   '''

#Linked list
class LList:
    def __init__(self,data):
       self.next=None
       self.data=data
       #print("Init LList")

    def addToLast(self,data):
        tmp=self;
        while(tmp.next):
            tmp=tmp.next
        tmp.next=LList(data)

    def show(self):
        temp=self;
        while(temp.next):
            print(temp.data,end='-->')
            temp=temp.next;
        print(temp.data)
