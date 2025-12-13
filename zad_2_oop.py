class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library in {self.city}, {self.street}, "
            f"{self.zip_code}, open hours: {self.open_hours}, "
            f"phone: {self.phone}"
        )


class Employee:
    def __init__(
            self, first_name, last_name, hire_date, birth_date, city,
            street, zip_code, phone
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"hired: {self.hire_date}, "
            f"phone: {self.phone}, "
            f"address: {self.city}, {self.street}, {self.zip_code}"
        )


class Book:
    def __init__(
            self, library, publication_date, author_name,
            author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book by {self.author_name} {self.author_surname}, "
            f"published: {self.publication_date}, "
            f"pages: {self.number_of_pages}, "
            f"available at: {self.library}"
        )


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(str(book) for book in self.books)

        return (
            f"Order date: {self.order_date}\n"
            f"Handled by: {self.employee}\n"
            f"Student: {self.student}\n"
            f"Books:\n{books_str}"
        )


library1 = Library(
    city="Katowice",
    street="Bankowa 5",
    zip_code="41-500",
    open_hours="Mon–Fri 8:00–16:00",
    phone="123456789"
)

library2 = Library(
    city="Bytom",
    street="Plac Sobieskiego",
    zip_code="41-902",
    open_hours="Mon–Fri 10:00–18:00",
    phone="327870601"
)

employee1 = Employee(
    first_name="Anna",
    last_name="Kowalska",
    hire_date="2021-05-01",
    birth_date="1995-03-12",
    city="Katowice",
    street="Bankowa 5",
    zip_code="41-500",
    phone="500600700"
)
employee2 = Employee(
    first_name="Maciej",
    last_name="Adamiec",
    hire_date="2019-04-01",
    birth_date="1994-08-11",
    city="Chorzów",
    street="Wolnosci 8",
    zip_code="41-501",
    phone="502468500"
)
employee3 = Employee(
    first_name="Zuzanna",
    last_name="Nowak",
    hire_date="2025-06-01",
    birth_date="1998-05-15",
    city="Katowice",
    street="Bankowa 5",
    zip_code="41-500",
    phone="500600700"
)

book1 = Book(
    library=library1,
    publication_date="2010-01-01",
    author_name="George",
    author_surname="Orwell",
    number_of_pages=328
)
book2 = Book(
    library=library2,
    publication_date="2000-06-01",
    author_name="Albert",
    author_surname="Camus",
    number_of_pages=294
)
book3 = Book(
    library=library1,
    publication_date="1999-01-01",
    author_name="Aleksander",
    author_surname="Fredro",
    number_of_pages=190
)
book4 = Book(
    library=library1,
    publication_date="1901-01-01",
    author_name="Stanisław",
    author_surname="Wystpiański",
    number_of_pages=180
)
book5 = Book(
    library=library1,
    publication_date="1889-01-01",
    author_name="Bolesław",
    author_surname="Prus",
    number_of_pages=380
)

student1 = Student(
    first_name="Alicja",
    last_name="Kowalska",
)
student2 = Student(
    first_name="Mateusz",
    last_name="Gola",
)
student3 = Student(
    first_name="Marta",
    last_name="Duda",
)

order1 = Order(
    employee=employee1,
    student=student1,
    books=[book1, book2],
    order_date="2025-10-10"
)
order2 = Order(
    employee=employee2,
    student=student2,
    books=[book3, book4, book5],
    order_date="2025-12-11"
)

print(order1)
print(order2)
