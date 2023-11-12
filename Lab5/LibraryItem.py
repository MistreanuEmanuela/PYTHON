class LibraryItem:
    def __init__(self, name, author, year, price):
        self._name = name
        self._author = author
        self._year = year
        self._price = price
        self._available = True

    def check_out(self):
        if self._available:
            self._available = False
            print(f"{self._name} was check_out")
        else:
            raise Exception("You don't have this item available now")

    def return_item(self, atribute1, atribute2):
        pass

    def display_information(self):
        pass


class Book(LibraryItem):
    def __init__(self, name, author, year, price, num_pages, wear, type_content):
        super().__init__(name, author, year, price)
        self._num_pages = num_pages
        self._wear = wear
        self._type = type_content
        self._available = True

    def return_item(self, num_pages, wear):
        if num_pages < self._num_pages or wear > self._wear + 0.10:
            return f"You can return {self._name}, it isn't in same wear as you check out, you need to pay {self._price}"
        else:
            if not self._available:
                self._available = True
                return f"{self._name} was returned"
            else:
                raise Exception(f"We already already received it")

    def display_information(self):
        return f"Book: {self._name}, author: {self._author}, type of book: {self._type} from year: {self._year}"


class DVD(LibraryItem):
    def __init__(self, name, director, year, price, dimension, wear, content):
        super().__init__(name, director, year, price)
        self._dimension = dimension
        self._wear = wear
        self._content = content

    def return_item(self, dimension, wear):
        if dimension != self._dimension or wear > self._wear + 0.10:
            raise Exception(f"You can return {self._name}, it isn't in same wear as you check out, you need to pay {self._price}")
        else:
            if not self._available:
                self._available = True
                return f"{self._name} was returned"
            else:
                raise Exception(f"We already already received it")

    def display_information(self):
        return f"DVD: {self._name}, director: {self._author},content {self._content}, from year: {self._year}"


class Magazine(LibraryItem):
    def __init__(self, name, year, price, num_pages, wear, content):
        super().__init__(name, "N/A", year, price)
        self._num_pages = num_pages
        self._wear = wear
        self._content = content

    def return_item(self, num_pages, wear):
        if num_pages != self._num_pages or wear > self._wear + 0.10:
            raise Exception(f"You can return {self._name}, it isn't in same wear as you check out, you need to pay {self._price}")
        else:
            if not self._available:
                self._available = True
                return f"{self._name} was returned"
            else:
                raise Exception(f"We already already received it")

    def display_information(self):
        return f"Magazine: {self._name}, author: {self._author},content {self._content}, from year: {self._year}"


book1 = Book("book1", "autor1", 1960, 21.5, 180, 0.01, "Comedie")
dvd1 = DVD("Dvd1", "Director", 2016, 17.0, "3D", 0.02, "desene animate")
magazine1 = Magazine("National Geographic", 2023, 5.0, 50, 0.1, "natura")

print(book1.display_information())
print(dvd1.display_information())
print(magazine1.display_information())

book1.check_out()
dvd1.check_out()
magazine1.check_out()
# book1.check_out()

print(book1.return_item(200, 0.07))
# print(dvd1.return_item("2D", 0.03))
print(magazine1.return_item(50, 0.15))


# print(book1.return_item(180, 0.05))
# print(dvd1.return_item("2D", 0.02))
# print(magazine1.return_item(50, 0.1))
