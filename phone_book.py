# Author: jerrybelmonte
# Implement a simple phone book manager.


class PhoneBook:
    def __init__(self):
        self.contacts = dict()

    def add(self, number: int, name: str):
        """Adds a contact to the phone book with the given name and number.
        If the number already exists, the contact name will be overwritten."""
        self.contacts[number] = name

    def erase(self, number: int):
        """Erases a person with the given number from the phone book if and
        and only if the contact number is in the phone book."""
        if number in self.contacts:
            del self.contacts[number]

    def find(self, number: int):
        """Looks for a person with the given phone number. Returns a string
        with the contact name, or 'not found' if the phone number is not in
        the phone book."""
        if number in self.contacts:
            return self.contacts.get(number)
        return 'not found'


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        self.name = None
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    phone_book = PhoneBook()

    for cur_query in queries:
        if cur_query.type == 'add':
            phone_book.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            phone_book.erase(cur_query.number)
        elif cur_query.type == 'find':
            result.append(phone_book.find(cur_query.number))

    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
