# this is a version of the list , but now build out
class MyCustomList:
    # defining the objects constructor , should be intialized with a dictionary and a default length
    def __init__(self):
        self.dictionary = {}
        self.length = 0


    #then we can define methods for interacting with the data
    def push(self,value):
        self.dictionary[self.length] = value
        self.length += 1


    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        return self.dictionary.pop(self.length)

newlist = MyCustomList()
newlist.push(1)
newlist.push("Joseph")
##checking length
## transverse or use index for items.
print(newlist.length)
print(newlist.pop())