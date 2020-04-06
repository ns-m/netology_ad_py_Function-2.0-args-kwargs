from classes.contact_class import Contact
from classes.phone_book_class import PhoneBook

contact_pb = Contact
phone_book = PhoneBook


def list_to_dict(any_list):
    new = {}
    if any_list[0] != '':
        for item in any_list:
            i = item.split('=')
            new[i[0]] = i[1]
    return new


if __name__ == '__main__':
    book_name = input('Phonebook name?: ')
    new_phone_book = phone_book(book_name)
    print(f'To work with |{book_name}| use the following commands: \n'
          f'Add - add contact\nList - display all contacts')
    print('Del - delete by phone number\nFavorites - show all selected contacts\n'
          'Search - search by first and last name\nExit - for quit')
    while True:
        command = input('\nEnter your command: ')
        print()
        if command == 'Add':
            f_name = input('Enter first name: ')
            if not f_name:
                print('This field is required')
            l_name = input('Enter last name: ')
            if not l_name:
                print('This field is required')
            t_number = input('Enter phone number: ')
            if not t_number:
                print('This field is required')
            chosen = input('Add contact to favorites? (yes/no): ').lower()
            if chosen == 'yes':
                chosen_con = True
            else:
                chosen_con = False
            additional_number = input('Additional contact numbers, separated by commas (optional field): ')\
                .replace(' ', '').split(',')
            additional_info_list = input('Additional information, separated by commas(example telegram=@test): ')\
                .replace(' ', '').split(',')
            additional_info = list_to_dict(additional_info_list)
            new_contact = contact_pb(f_name, l_name, t_number, chosen_con, *additional_number, **additional_info)
            new_phone_book.add_contact(new_contact)

        elif command == 'List':
            new_phone_book.all_contacts()

        elif command == 'Del':
            contact_for_del = input('Enter the phone number of the contact to delete: ')
            new_phone_book.del_by_number(contact_for_del)
            print(f'Contact with phone number {contact_for_del} deleted')

        elif command == 'Favorites':
            new_phone_book.all_chosen()

        elif command == 'Search':
            f_name = input('Enter first name: ')
            l_name = input('Enter last name: ')
            print()
            new_phone_book.search_by_name(f_name, l_name)

        elif command == 'Exit':
            break

        else:
            print('Invalid Command')