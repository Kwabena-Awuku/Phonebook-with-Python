'''
Phonebook Application

Introduction:
Build a simple phonebook application using Python. 
This application allows users to add contacts with their phone numbers, search for a contact by name, display all contacts, 
 delete any contact and quit the application using Python dictionaries. 
Upon running the program, users will see a menu displaying the following options:

Find the requirements for the program below. The program should: 
1.Add a contact
2.Search for a contact
3.Display all contacts
4.Delete a contact
5.Quit

Option 1 prompts users to enter the name and phone number of the contact to add, stored in a dictionary.
Option 2 prompts users to enter the name of the contact to search for. 
If found, it displays the contact's name and phone number; otherwise, it indicates that the contact was not found.
Option 3 displays all contacts stored in the phonebook dictionary, or indicates if it's empty.
Option 4 delete a contact stored in the phonebook dictionary
Option 5 terminates the application.


'''


#Initializing an empty dictionary to store contacts

phone_book = {}



while True:
    #Display menu options
    print("\nPhonebook Application")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Display all contacts")
    print("4. Delete a contact")
    print("5. Quit")

#get users' choice
    choice = input("Entet An Option(1 - 4):")
    
    print()
    if choice == "1": #Add a contact
        name = input("Enter the contact name:").strip().lower()
        phone = (input("Enter the phone number:")).strip()
        if name in phone_book:
            print(f"The contact '{name}' already exists. Updating the phone number")
        phone_book[name] = phone
        print(f"The contact '{name}' has been added successfully.")
        
        
    elif choice == "2": #Search for contact
        name = input("Please enter the name of the contact you want to find:")
        if name in phone_book:
            print(f"Name: '{name}, Phone: {phone_book[name]}'")
        else:
            print(f"The contact '{name}' wasn't found")
            
    elif choice == "3":  #Display all contacts
        if phone_book:
            print("\nAll Contacts:")
        for name, phone in phone_book.items():
            print(f"Name: {name}, Phone: {phone}" )
        
        else:
            print("PhoneBook is empty.")
    elif choice =="4": #Delete a contact
        name = input ("Enter the name of the contact to delete:").strip().lower()
        if name in phone_book:
            del phone_book[name]
            print(f"The contact {name} has been deleted successfully")
            
    elif choice == "5":
        print("Exiting the phonebook application. Goodbye!!")
        break
    
    else:
        print("Invalid choice. Please select a valid option (1 - 4.)")
            
            
            
            
 