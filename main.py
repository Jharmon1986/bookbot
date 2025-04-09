def get_book_text(filepath):
    # This function reads the content of a book file and returns it as a string.
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

from stats import accept_book_text #imports accept_book_text function from stats.py
from stats import text_to_char #imports text_to_char function from stats.py

def print_report(path, word_count, sorted_chars):
    # Print the full formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    
    print("============= END ===============")

def main():
    # Specify the relative path to the book file
    relative_path = 'books/frankenstein.txt'  # Adjust this if the file is in a subdirectory
    # Call the get_book_text function to read the file's content
    book_text = get_book_text(relative_path)
    # Pass the book text to accept_book_text to process it
    word_count = accept_book_text(book_text)
    char_count = text_to_char(book_text)  # Call the text_to_char function to process the book text
    print(char_count)
if __name__ == '__main__':
    main()





