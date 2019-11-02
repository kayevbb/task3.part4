class ContactList(list):
    def __init__(self, *all):
        self.all = all

    def search_by_name(self, search_name):

        for name in self.all:
            if name == search_name:
                print(name)


contacts = ContactList('Айбек', 'Нурбек', 'Илзат', 'Дастан')
contacts.search_by_name('Бектур')































