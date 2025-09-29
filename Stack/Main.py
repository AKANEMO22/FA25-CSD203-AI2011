from Stack import Stack
def Dec2Bin(x):
    myStack=Stack()
    while (x!=0):
        b=x%2
        myStack.push(b)
        x=int(x/2)
    while not myStack.isEmpty():
        print(myStack.pop(),end='')

def reverseString(str):
    myStack=Stack()
    for s in str:
        myStack.push(s)
    rs = ""
    while not myStack.isEmpty():
        rs += myStack.pop()
    return rs    
    
# x=int(input("Input number to convert to Binary: "))
# Dec2Bin(x)
str=input("Input a string to reverse: ")
print(reverseString(str))        
        
