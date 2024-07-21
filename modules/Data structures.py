'''class MyClass:
    def __init__(self, data):
        self.data = data    #getting data  storing  as list tuples iteratbles

    def __iter__(self):     #  this is not like init no automatically call by durirng  object creation
                            #rather is is invoked  by for loop it return the iterator object to forloop
        return iter(self.data)  #it is called when object is iteration context  like for loop

    def iter(self):   #   normal methods called by object of this class
        # Some code to generate an iterator object
        return iter(self.data) #--- this iter is builin  this retunr the oriiginal  iiterator object
                                # by taking data as a parameter
            # it retunr the iterator object

my_object = MyClass((1, 2, 3, 4, 5))   #object createing


my_class = [1,2,2,3,34,4,2]

iterator =   iter(my_class)   #this function return a  original object iterator object itself
#object  == method(data)

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

a =my_object.iter()  # this is object methods it call another buildin function there

print(my_object.data)
b = my_object.__iter__()  # does the same thing but we define this with a class to cusctomise the iterations

print("this is  __ITER__  =====>  "+ str(b.__next__()))


for loop i in  myobject == for loop calls the __iter__ by itself  


print(my_object.iter()) # i can explicitly call this method here

print(next(a))
print(my_object)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

'''

#linked list

#  a variable able to store the address of the object then it act as that object

class Node:
     def __init__(self, data= None, next=None):
         self.data = data
         self.next = next

class List:
    def __init__(self):
        self.head = None
                                        # object means  a memory allocation is happening then the address
                                        # of memory given to that object just a pointer
    def create_at_begin(self, data):         # object just acting as a pointer p->
        node = Node(data,self.head)         # this  object node has address for this structures
        self.head  = node                   # just passing the address to head varibale
                                           # now head is the node object self refers selfish


    def iter(self):
        itr = self.head

        while itr:                  # we just need node object not node next
            print(itr.data)
            itr = itr.next         # .next = contaion object of next node im giving that to itr variable
                                    # changing itr normal varibla to pointer like object


    def creat_at_end(self, x):
        if self.head is None:
            self.head = Node(x, None)
            return
        itr = self.head
        while itr.next  :

            itr = itr.next

        itr.next = Node(x,None)     # we directlyt creatiing object and give address to previos node next


# self.head.next  =  which is like 1st 2nd node  next --value directly we can able to access
# itr.next(1stnode) = itr.next.next(2ndNodevalue) = also same
lit = List()

#lit.create_at_begin(5)
#lit.create_at_begin(4)
lit.create_at_begin(3)
lit.creat_at_end(10)
lit.creat_at_end(4)
lit.creat_at_end(5)

lit.iter()



'''         TREEE       DATASTRUCTURE   

file storage system is  using this data structure here  

'''

# each node must have onlyu one edge root node no edge  no of node (n) no of edge = n-1



















