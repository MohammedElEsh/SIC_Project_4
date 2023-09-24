class Stack:
    def __init__(self):             # contructor
        self.items = []



    def isEmpty(self):              # method
        return self.items == []
    


    def push(self , item):          # method
        self.items.append(item)



    def pop(self):                  # method

        # return None if self.isEmpty() else self.items.pop()
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):                 # method

        # return None if self.isEmpty() else self.items[-1]
        if self.isEmpty():
            return None
        else:
            return self.items[-1]



