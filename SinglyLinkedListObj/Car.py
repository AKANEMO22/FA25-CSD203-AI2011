class Car:
    def __init__(self, id, name, price):
        self.id=id
        self.name=name
        self.price=price
        
    def __str__(self):
        return f"{self.id:<5} {self.name:<25} {self.price:^9}";
