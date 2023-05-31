class library:
    pass
    def __init__(self,listOfBooks):
        self.books= listOfBooks
        
    def displayAvailableBooks(self):
        print("Books present in the Library are : ")
        for book in self.books:
            print('\t' + book)
            
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
        else:
            print("sorry, this book has already been taken. Kindly wait for its return.")
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book! Hope you enjoyed reading it.")
            
class Student:
         
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")
        return self.book

if __name__ == " __main__ ":
    centeraLibrary = library(["Applied Physics","Calculus","Python","C++","Machine Learning","Computer Networks"])
    centeraLibrary.displayAvailableBooks()
    while(True):
        
        welcomeMsg = '''====== Welcome to centeral Library =====
        please choose an option:
        1. List all the books.
        2. Request a book.
        3. Return a book.
        4. Exit a library.
        '''
        print(welcomeMsg)
        student = student()
        a = int(input("Enter a choice: "))
        if a == 1:
            centeraLibrary.displayAvailableBooks()
        elif a == 2:
            centeraLibrary.borrowBook(Student.requestBook())
        elif a == 3:
            centeraLibrary.returnBook(Student.returnBook())
        elif a == 4:
            print("Thanks for using the library")
            exit()
        else:
            print("Invalid Choice!")
        
        