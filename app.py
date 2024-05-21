from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class Book:
    title: str
    author: str
    year: str
    isbn: str

    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn 

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}"


book = Book(title="1984", author="Geoge Orrwell", year=1949, isbn="123-456-78")
print(book.display_details())

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book_by_isbn(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def display_all_books(self):
        for book in self.books:
            print(book.display_details())

library = Library()
book1 = Book(title="1985", author="Muslim Uwi", year=1949, isbn="123-456-708")
book2 = Book(title="1986", author="Ahmed adit", year=1949, isbn="123-456-789")

library.add_book(book1)
library.add_book(book2)

library.display_all_books()

library.remove_book_by_isbn("123-456-789")
library.display_all_books()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"


person = Person(name="Alice", age=30)
student = Student(name="Alice", age=30, student_id="S12345")

print(person.display_details())
print(student.display_details())


book_years = [book1.year, book2.year]
book_titles = [book1.title, book2.title]
plt.figure(figure=(10, 6))
plt.bar(book_titles, book_years, color="blue")

plt.xlabel("book title")
plt.ylabel("publication year")
plt.title("Books and their publication years")

plt.show()
