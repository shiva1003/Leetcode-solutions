class MyQueue:

    def __init__(self):
        self.q = []
        
    def push(self, x: int) -> None:   # Push element x to the back of queue...
        self.q.append(x)
        
    def pop(self) -> int:    	# Remove the element from the front of the queue and returns it...
          if len(self.q) > 0:
            return self.q.pop(0)
        
    def peek(self) -> int:   # Get the front element...
        return self.q[0]
        

    def empty(self) -> bool:   # Return whether the queue is empty...
        return len(self.q) == 0  
    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

