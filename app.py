import xml.etree.ElementTree as ET

# load the xml file
tree = ET.parse('books.xml')
root = tree.getroot()

# print the root tag
print(root.tag)

# # Iterate through books and print details
# for book in root.findall("book"):
#     title = book.find("title").text
#     author = book.find("author").text
#     year = book.find("year").text
#     print(f"Title: {title}, Author: {author}, Year: {year}")


# # Change the year of the first book
# first_book = root.find("book")
# first_book.find("year").text = "1926"  # Modify year


# # Save changes back to the file
# tree.write("books_modified.xml")
# print("XML file updated!")


# # Iterate through all book elements
# for book in root.findall("book"):
#     if book.get("id") == "102":
#         title = book.find("title").text
#         author = book.find("author").text
#         year = book.find("year").text
#         print(f"Book Found:\nTitle: {title}\nAuthor: {author}\nYear: {year}")
#         break
# else:
#     print("Book not found!")


# # Create a new book element
# new_book = ET.Element("book")
# new_book.set("id", "103")  # Setting the 'id' attribute

# # Add sub-elements (title, author, year)
# ET.SubElement(new_book, "title").text = "To Kill a Mockingbird"
# ET.SubElement(new_book, "author").text = "Harper Lee"
# ET.SubElement(new_book, "year").text = "1960"

# # Add the new book to the root
# root.append(new_book)

# # Save the updated XML file
# tree.write("books_modified.xml")
# print("New book added!")


# import xml.etree.ElementTree as ET

# # Create the root element
# root = ET.Element("library")

# # Create a book element with an id
# book1 = ET.SubElement(root, "book", id="101")
# ET.SubElement(book1, "title").text = "The Great Gatsby"
# ET.SubElement(book1, "author").text = "F. Scott Fitzgerald"
# ET.SubElement(book1, "year").text = "1925"

# # Create another book element
# book2 = ET.SubElement(root, "book", id="102")
# ET.SubElement(book2, "title").text = "1984"
# ET.SubElement(book2, "author").text = "George Orwell"
# ET.SubElement(book2, "year").text = "1949"

# # Convert the structure to an ElementTree object
# tree = ET.ElementTree(root)

# # Save to an XML file
# tree.write("books.xml", encoding="utf-8", xml_declaration=True)

# print("XML file 'books.xml' created successfully!")


# Create and write to a file using 'with' statement
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

# Read the file and demonstrate `tell()` and `seek()`
with open("example.txt", "r") as file:
    print("Reading file content:")
    print(file.read())  # Read the entire file
    print(f"Current position: {file.tell()}")  # Get current cursor position

    # Move the cursor back to the beginning using `seek()`
    file.seek(0)
    print(f"After seeking, current position: {file.tell()}")

    # Read the first line again
    print("First line:", file.readline().strip())

# Append new data to the file
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

# Verify that the new data has been added
with open("example.txt", "r") as file:
    print("\nUpdated file content:")
    print(file.read())  # Read updated content

# ====================================================

# Step 1: Create and write initial content
with open("example.txt", "w") as file:
    file.write("Line 1: Hello, World!\n")
    file.write("Line 2: Python is great.\n")
    file.write("Line 3: Have a nice day.\n")

# Step 2: Read the file content into a list
with open("example.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list

# Step 3: Insert new data at a specific position (e.g., after Line 1)
insert_position = 1  # Index where we want to insert
lines.insert(insert_position, "Line 1.5: Inserting a new line here!\n")

# Step 4: Write the modified content back to the file
with open("example.txt", "w") as file:
    file.writelines(lines)  # Write the modified list back to the file

# Step 5: Read the updated file to verify the change
with open("example.txt", "r") as file:
    print("\nUpdated File Content:")
    print(file.read())

# ====================================================

# Creating a sample file
with open("sample.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

# Reading the file using readline()
with open("sample.txt", "r") as file:
    print(file.readline())  # Reads the first line
    print(file.readline())  # Reads the second line


# ================================================================
# Writing multiple lines at once
lines = ["Line 1: Hello\n", "Line 2: Python\n", "Line 3: File Handling\n"]

with open("output.txt", "w") as file:
    file.writelines(lines)  # Writes all lines to the file at once

# Verifying by reading the file
with open("output.txt", "r") as file:
    print(file.read())
