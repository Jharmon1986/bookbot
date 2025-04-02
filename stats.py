def accept_book_text(file_contents):
    #this function accepts the book text and gets a word count
    word_count = len(file_contents.split())
    print(f"{word_count} words found in the document.")
    return file_contents  # Return the book text as a string