book_path = "books/frankenstein.txt"

def main():

    text = get_book_text(book_path)
    #print(text)

    words = word_count(text)
    #print(f"{words} words found in the document")

    chars = character_count(text)
    #print(chars)

    report_gen(book_path, words, chars)

    return text, words, chars
   

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    #count words in provided text file
    text_split = text.split()
    return len(text_split)


def character_count(text):
    #count instances of each character and put in dictionary string>integer     
    chars = {}
    for char in text.lower():
        if char.isalpha():
            chars[char] = chars.get(char, 0) +1
    return chars
    

def char_freq_sort(chars):
    # Convert dictionary to a list of dictionaries and sort by frequency
    char_list = [{"char": char, "count": count} for char, count in chars.items()]
    sorted_chars = sorted(char_list, key=lambda item: item["count"], reverse=True)
    return sorted_chars


def report_gen(book_path, words, chars):
    #print report to cmd line
    print(f"(*0_0)/   Report for ../{book_path}   \\(0_0*)\n")

    print(f"{words} words found in the document\n")

    print("Character counts:")
    for char, freq in sorted(chars.items()):
        print(f"The letter '{char}' appears {freq} times.")

    print("\nCharacter counts qty sort:")
    sorted_chars = char_freq_sort(chars)
    for item in sorted_chars:
        print(f"The letter '{item['char']}' appears {item['count']} times.")
    
    print(f"\n(*0_0)/   |          FIN          |   \\(0_0*)")


main()
