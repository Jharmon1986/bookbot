def accept_book_text(file_contents):
    #this function accepts the book text and gets a word count
    word_count = len(file_contents.split())
    print(f"Found {word_count} total words.")
    return word_count  # Return the word count

def text_to_char(file_contents):
    #This function takes the book text and converts it to the number of times each character appears in the text
    char_count = {}
    for char in file_contents:
        char = char.lower()  # Convert to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count  # Return the character count as a dictionary