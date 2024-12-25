# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price

        self.author= author

        self.chapters = []

    def addchapter(self,chapter):
        self.chapters.append(chapter)

    def pagecount(self):
        count=0
        for ch in self.chapters:
            count+= ch.pages
        return count


class author:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

class chapter:
    def __init__(self,chaptername,pages):
        self.chaptername=chaptername
        self.pages=pages
    
        
b1 = Book("War and Peace", 39.0, author("Leo", "Tolstoy"))
b1.addchapter(chapter("Chapter 1", 125))
b1.addchapter(chapter("Chapter 2", 97))
b1.addchapter(chapter("Chapter 3", 143))

print(b1.title)
print(b1.author.__dict__)
print(b1.author.fname)
print(b1.pagecount())
