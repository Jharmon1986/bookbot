import sys

#Check if user provided book path as argument
if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

    
def get_book_text(filepath):
    # This function reads the content of a book file and returns it as a string.
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

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

from stats import accept_book_text, text_to_char, sort_chars  # Import sort_chars

def main():
    # Specify the relative path to the book file
    relative_path = sys.argv[1]  # Get the book path from command line argument
    
    # Read the file's content
    book_text = get_book_text(relative_path)
    
    # Get word count
    word_count = accept_book_text(book_text)
    
    # Get character counts
    char_count = text_to_char(book_text)
    
    # Sort the character counts
    sorted_chars = sort_chars(char_count)
    
    # Print the formatted report
    print_report(relative_path, word_count, sorted_chars)

if __name__ == '__main__':
    main()





