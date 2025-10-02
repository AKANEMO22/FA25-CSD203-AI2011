def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def fibonacii(n):
    if n<2:
        return n
    else:
        return fibonacii(n-1)+fibonacii(n-2)
    
def HaNoiTower(n, s, d, m):
    if n==1:
        print(f"Move disk {n} from {s} to {d}")
    else:
        HaNoiTower(n-1, s, m, d)
        print(f"Move disk {n} from {s} to {d}")
        HaNoiTower(n-1, m, d, s)
        
n=int(input("Input n = "))
print(f"{n}! = {factorial(n)}")
for i in range (n):
    print(fibonacii(i), end=' ')
print()
HaNoiTower(3, 'A', 'C', 'B')