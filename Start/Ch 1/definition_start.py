# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  Book_Type=["COMIC","HOLLY"]
  def __init__(self,title,price):
    self.title=title
    self.price=price

  #instance method
  def change_title(self,title):
    self.title=title


# TODO: create instances of the class
b1=Book("The magic of big thinking",25)


# TODO: print the class and property
print(b1)
print(b1.title)
