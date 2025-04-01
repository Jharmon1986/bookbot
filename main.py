def get_book_text(filepath):
    # This function reads the content of a book file and returns it as a string.
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents


def accept_book_text(file_contents):
    #this function accepts the book text and gets a word count
    word_count = len(file_contents.split())
    print(f"{word_count} words found in the document.")
    return file_contents  # Return the book text as a string

def main():
    # Specify the relative path to the book file
    relative_path = 'books/frankenstein.txt'  # Adjust this if the file is in a subdirectory
    # Call the get_book_text function to read the file's content
    book_text = get_book_text(relative_path)
    # Pass the book text to accept_book_text to process it
    accept_book_text(book_text)
    
if __name__ == '__main__':
    main()





