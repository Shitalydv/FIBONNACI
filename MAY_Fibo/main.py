books=[]

def list_book():
    return(books)
    
def add_books(name, auther, price, p_year):
    book = {
        "name":name,
        "auther": auther,
        "price": price,
        "published_year": p_year       
    }
    books.append(book)
    return True

def get_book(name):
    for book in books:
        if book["name"]==name:
            return book    
    

def main():
    while True:
        print("Starting book management system...")
        
        print("ENter l for getting book list")
        print("enter n for adding new book ")
        print("Enter d for book details")
        print("enter x for deleting book")
        print("enter e for editing book information")
        print("enter q for exiting the aplication")
        user_input=input("User input: ")
        if user_input=='l':
            all_books=list_book()
            for book in all_books:
                print(all_books)
        elif user_input=="n":
            book_name=input("Entr book name:")
            auther=input("Enter auther's name:")
            price=int(input("Enter price of book:"))
            p_year=input("Enter the year when it was published:")
            add_books(book_name, auther, price, p_year)
            
    
        elif user_input=="d":
            ...
        elif user_input=="x":
            ...
        elif user_input=="e":
            book_name=input("ENter book name: ")
            
        elif user_input=="q":
            exit()
        else:
            print("Your input is invalid")
        
        
        
        
main()