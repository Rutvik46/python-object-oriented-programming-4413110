# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title,price):
        self.title = title
        # TODO: add properties
        self.price=price
        self.__secret="this is a secret attribute"

    # TODO: create instance methods
    def set_disccount(self,discount):
        self._discount=discount

    def get_price(self):
        if hasattr(self,"_discount"):
            self.price=self.price - self.price * self._discount
            return self.price
        else:
            return self.price

# TODO: create some book instances
b1 = Book("War and Peace",25)
b2 = Book("The Catcher in the Rye",30)

# TODO: print the price of book1
print(b1.price)

# TODO: try setting the discount
print(b2.get_price())
b2.set_disccount(0.40)
print(b2.get_price())

# TODO: properties with double underscores are hidden by the interpreter
print(b1.__secret)