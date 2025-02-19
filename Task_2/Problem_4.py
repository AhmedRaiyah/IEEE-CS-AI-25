
library_catalogue = {}

num_of_books = int(input("Enter the # of books: "))

for book in range(num_of_books):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")

    library_catalogue[title] = {"author": author, "year": year}

print("Library Catalogue")
print("---------------")
for title, details in library_catalogue.items():
    print(f"{title} - Author: {details['author']}, Year: {details['year']}")
