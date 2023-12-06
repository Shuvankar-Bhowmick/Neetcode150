'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
 
'''
class MinStack:

    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._stack.append((val, val))
        else:
            minimum = self.getMin()
            self._stack.append((val, min(val, minimum)))

    def pop(self) -> None:
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        _, _min = self._stack[-1]
        return _min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()