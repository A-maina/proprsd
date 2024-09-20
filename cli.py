from Book import  Book
from Member import Member
from Borrowing import Borrowing
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Member")
        print("2. View Members")
        print("3. Edit Member")
        print("4. Delete Member")
        print("5. Add Book")
        print("6. View Books")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter member name: ")
            member = Member(name)
            member.save()
            print(f"Member {name} added.")
            
        elif choice == "2":
            members = Member.fetch_all()
            print("Members:")
            for member in members:
                print(f"ID: {member.id}, Name: {member.name}")
                
        elif choice == "3":
            member_id = int(input("Enter member ID to edit: "))
            new_name = input("Enter new name: ")
            Member.update(member_id, new_name)
            print("Member updated.")
            
        elif choice == "4":
            member_id = int(input("Enter member ID to delete: "))
            Member.delete(member_id)
            print("Member deleted.")
            
        elif choice == "5":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book = Book(None, title, author)
            book.save()
            print(f"Book '{title}' by {author} added.")
            
        elif choice == "6":
            books = Book.fetch_all()
            print("Books:")
            for book in books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {status}")
                
        elif choice == "7":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID to borrow: "))
            borrowing = Borrowing(None, book_id, member_id)
            borrowing.save()
            print(f"Book {book_id} borrowed by member {member_id}.")
            
        elif choice == "8":
            book_id = int(input("Enter book ID to return: "))
            Borrowing.return_book(book_id)
            print(f"Book {book_id} returned.")
            
        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")
            
if __name__ == "__main__":
    Member.create_table()
    Book.create_table()
    Borrowing.create_table()
    main_menu()
