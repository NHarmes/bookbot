def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count = word_count(text)
    print(f"{count} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    text_split = text.split()
    return len(text_split)
    

main()
