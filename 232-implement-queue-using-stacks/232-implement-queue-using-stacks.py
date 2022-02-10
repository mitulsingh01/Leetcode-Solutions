class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self._reverseStack()
        return self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self._reverseStack()
        return self.stack2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return True
            else:
                return False
        
    def _reverseStack(self):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return None
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()