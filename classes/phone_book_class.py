class PhoneBook:
    contact_list = []

    def __init__(self, name):
        self.name = name

    def all_contacts(self):
        if len(self.contact_list) > 0:
            for contact in self.contact_list:
                print(contact)
        else:
            print ('Phone book is empty')

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def del_by_number(self, tel_number):
        for contact in self.contact_list:
            if contact.tel_number == tel_number:
                self.contact_list.remove(contact)
            else:
                return None

    def all_chosen(self):
        for contact in self.contact_list:
            if contact.chosen_contact:
                print(contact)

    def search_by_name(self, first_name, last_name):
        for contact in self.contact_list:
            if first_name == contact.first_name and last_name == contact.last_name:
                print(contact)