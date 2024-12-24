# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  Book_Type=["COMIC","HOLLY"]
  def __init__(self,title,author):
    self.title=title
    self.author=author

  #instance method
  def get_book_title(self):
    return self.title


# TODO: create instances of the class
b1=Book("The magic of big thinking","None")


# TODO: print the class and property
print(b1)
print(b1.title)
