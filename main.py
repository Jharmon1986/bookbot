def get_book_text(filepath):
    # This function reads the content of a book file and returns it as a string.
    
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

def main():
    # Specify the relative path to the book file
    relative_path = 'books/frankenstein.txt'  # Adjust this if the file is in a subdirectory
    # Call the get_book_text function to read the file's content
    book_text = get_book_text(relative_path)
    # Print the content of the book to the console
    print(book_text)

if __name__ == '__main__':
    main()

