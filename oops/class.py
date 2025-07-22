class car:

    def __init__(self,brand,year):
        self.brand = brand
        self.year = year


    def describe(self):
        print(f"This car is a {self.year} {self.brand}.")


car1 = car("maruti", 2025)
car1.describe() 