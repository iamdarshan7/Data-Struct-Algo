class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)        

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def count(self):
        return len(self.items)  

# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol in "([{":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top, symbol):
#                     balanced = False
#         index += 1

#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False  

# def matches(open, close):
#     opens = '([{'
#     closer = ')]}'
#     return opens.index(open) == closer.index(close)

# print(parChecker('(())'))
# print(parChecker('(()))'))
# print(parChecker('{({([][])}())}'))
# print(parChecker('[{()]'))























# # Python3 program to print the elements of a  
# # stack from bottom to top  
  
# # Stack class with all functionality of a stack 
# # import sys 
# class Stack: 
#     def __init__(self): 
#         self.s = [] 
  
#     def push(self, data): 
#         self.s.append(data) 
      
#     def pop(self): 
#         return self.s.pop() 
  
#     def peek(self): 
#         return self.s[-1] 

#     def count(self): 
#         return len(self.s) 
  
# # # Recursive function to print stack elements  
# # # from bottom to top without changing  
# # # their order  
# # def printStack(s): 
      
# #     # if stack is empty then simply return 
# #     if s.count() == 0: 
# #         return
# #     x = s.peek() 
  
# #     # pop top most element of the stack 
# #     s.pop() 
      
# #     # recursively call the function printStack 
# #     printStack(s) 
      
# #     # Print the stack element starting  
# #     # from the bottom  
# #     print("{} ".format(x), end = "") 
      
# #     # Push the same element onto the stack  
# #     # to preserve the order  
# #     s.push(x) 
  
# # # Driver code 
# # if __name__=='__main__': 
# #     s=Stack() 
# #     s.push(1) 
# #     s.push(2) 
# #     s.push(3) 
# #     s.push(4) 
  
# #     printStack(s) 
  