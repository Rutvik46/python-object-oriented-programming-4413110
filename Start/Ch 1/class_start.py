# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods

class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPE=["MOTIVATIONAL","COMIC","HOLLY"]

    # TODO: double-underscore properties are hidden from other classes
    __BOOKLIST=None

    # TODO: create a class method
    @classmethod
    def get_book_type(cls):
        return cls.BOOK_TYPE

    # TODO: create a static method
    @staticmethod
    def get_book_list():
        if Book.__BOOKLIST==None:
            Book.__BOOKLIST=[]
        return Book.__BOOKLIST

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title,booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPE):
            raise ValueError("{booktype} is not a valid book type")
        else:
            self.booktype=booktype

# TODO: access the class attribute
print("Book Type:",Book.get_book_type())
book_type=Book.get_book_type()
book_type.append("ACADEMIC")
print("Book Type:",Book.get_book_type())

# TODO: Create some book instances
b1=Book("The Gita","HOLLY")
b2=Book("The Magic of Big Thinking","MOTIVATIONAL")

print(b1)
print(b1.title)
print(b1.booktype)
print(b1.BOOK_TYPE)
#print("Book List:", b1.__BOOKLIST)
print("Book List:", b1._Book__BOOKLIST)

# TODO: Use the static method to access a singleton object
book_list=Book.get_book_list()
book_list.append(b1)
print("Book List:", Book.get_book_list())

Book.name=[]
Book.name.append(b1)
print(b1.name)