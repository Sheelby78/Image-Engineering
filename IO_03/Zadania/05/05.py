class Product:
    name = None
    price = None
    quantity = None

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name + " " + str(self.price)

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

    def __str__(self):
        Content = ""
        for i in self.List:
            Content += i.name + " " + str(i.quantity) + ", "
        return Content

    def __len__(self):
        total = 0
        for i in self.List:
            total += i.quantity
        return total

    def __iter__(self):
        self.currentIndex = 0
        return self

    def __next__(self):
        if self.currentIndex < len(self.List):
            x = self.List[self.currentIndex]
            self.currentIndex += 1
            return x
        raise StopIteration



koszyk = Cart()
p = Product('Orzech', 20, 2)
print(str(p))
print(str(koszyk))
print(len(koszyk))

for produkt in koszyk:
    print(produkt)
