from Stack import Stack
def Dec2Bin(x):
    myStack=Stack()
    while (x!=0):
        b=x%2
        myStack.push(b)
        x=int(x/2)
    while not myStack.isEmpty():
        print(myStack.pop(),end='')
        
x=int(input("Input number to convert to Binary: "))
Dec2Bin(x)      
        
