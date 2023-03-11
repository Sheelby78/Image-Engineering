class Product:
    name = None
    price = None
    quantity = None

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    List = [Product('Pomidor', 10, 2), Product('Jablko', 2, 1), Product('Gruszka', 3, 3), Product('Ogorek', 2, 1),
            Product('Marchew', 15, 2)]

    def add(self, name):
        for i in self.List:
            if i.name == name:
                i.quantity += 1
                break

    def remove(self, name):
        for i in self.List:
            if i.name == name and i.quantity != 0:
                i.quantity -= 1
                if i.quantity == 0:
                    self.List.remove(i)
                break
    def total_price(self):
        total = 0
        for i in self.List:
            total += i.quantity * i.price
        return total

c = Cart()
print("\nPoczatkowy stan koszyka:")
for i in c.List:
    print(i.name, i.quantity)

c.add('Pomidor')
c.add('Jablko')
c.add('Gruszka')
c.add('Ogorek')
c.add('Ogorek')
c.add('Marchew')
c.add('Gruszka')
c.remove('Jablko')
c.remove('Marchew')
c.remove('Ogorek')

print("\nStan koszyka po zmianach:")
for i in c.List:
    print(i.name, i.quantity)

print("\nWartosc koszyka: ", c.total_price())
