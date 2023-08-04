from AddressBook import *


class Bot:
    def __init__(self):
        self.book = AddressBook()
        self.load_book = Load()

    def add(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        add_cl = Add()
        return add_cl.add(record)


    def search(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        search_book = Search()
        result = (search_book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)
    
    
    def edit(self):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        edit_book = Edit()
        return edit_book.edit(contact_name, parameter, new_value)


    def remove(self):
        pattern = input("Remove (contact name or phone): ")
        remove_book = Remove()
        return remove_book.remove(pattern)


    def save(self, file_name):
        file_name = input("File name: ")
        save_book = Save()
        return save_book.save(file_name)
    

    def load(self):
        file_name = input("File name: ")
        return self.load_book.load(file_name)
    

    def congratulate(self):
        congratulate_contact = Congratulate()
        print(congratulate_contact.congratulate())
    

    def view(self):
        print(self.book)


    def handle(self, action):
        if action == 'add':
            return self.add()   
        elif action == 'search':
            self.seacrh()
        elif action == 'edit':
            self.edit()
        elif action == 'remove':
            self.remove()
        elif action == 'save':
            self.save()
        elif action == 'load':
            self.load()
        elif action == 'congratulate':
            self.congratulate()
        elif action == 'view':
            self.view()
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")
