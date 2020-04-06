class Contact:

    def __init__(self, first_name, last_name, tel_number, chosen_contact=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.tel_number = tel_number
        self.chosen_contact = chosen_contact
        self.additional_info = {}
        self.additional_info.setdefault('Additional numbers', args)
        for key, value in kwargs.items():
            self.additional_info.update({key: value})

    def __str__(self):
        numbers = ' '
        all_string = 'First name: {}\nLast name: {}\nTelephone number: {}\n'.format(self.first_name, self.last_name, self.tel_number)
        if not self.chosen_contact:
            all_string += 'In favorites: no\nAdditional Information:\n'
        else:
            all_string += 'In favorites: yes\nAdditional Information:\n'
        if self.additional_info:
            for key, value in self.additional_info.items():
                if key == 'Additional numbers' and value[0] != '':
                    for item in value:
                        numbers += item + '; '
                    all_string += '\t{}: {}\n'.format(key, numbers)
                elif value[0] == '':
                    continue
                else:
                    all_string += '\t{}: {}\n'.format(key, value)
        return all_string