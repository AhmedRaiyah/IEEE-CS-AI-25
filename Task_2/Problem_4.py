
library_catalog = {}

num_of_books = int(input("Enter the # of books: "))

for book in range(num_of_books):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")

    library_catalog[title] = {"author": author, "year": year}

print("---------------")
for title, details in library_catalog.items():
    print(f"{title} - Author: {details['author']}, Year: {details['year']}")
