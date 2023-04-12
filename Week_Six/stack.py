class Stack:
    def __init__(self, size):
        self.starr = []
    def push(self,item):
        self.starr.append(item)
    def pop(self):
        return self.starr.pop()
    def is_empty(self):
        if len(self.starr) == 0:
            return 1
        else:
            return 0
        
