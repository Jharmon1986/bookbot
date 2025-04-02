def get_book_text(filepath):
    # This function reads the content of a book file and returns it as a string.
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

from stats import accept_book_text

def main():
    # Specify the relative path to the book file
    relative_path = 'books/frankenstein.txt'  # Adjust this if the file is in a subdirectory
    # Call the get_book_text function to read the file's content
    book_text = get_book_text(relative_path)
    # Pass the book text to accept_book_text to process it
    accept_book_text(book_text)
    
if __name__ == '__main__':
    main()





