import sys

if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)  
    word_count = get_word_count(text)
    charsdict = get_char_count(text)
    sortcharacters = sort_char_count(charsdict)

    #layout
    print ("========Bookbot========")
    print (f"Analyzing book found at; {book_path}...\n")
    print ("------Word Count-------")
    print (f"{word_count} words found in the document\n")
    print ("----Character Count----") 
    #print (sortcharacters)
    for item in sortcharacters:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print ("==========END==========")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_word_count, get_char_count, sort_char_count

main()