
# count words in doc
def get_word_count(text):
    words = text.split()
    return len(words)

# count characters in doc, output dictionary
def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# sort char dictionary, bin special chars, and sort by highest count to lowest

def sort_on(d):
    return d["num"]

def sort_char_count(chars_dict):
    sortedchars = []
    for ch in chars_dict:
        sortedchars.append({"char": ch, "num": chars_dict[ch]})
    sortedchars.sort(reverse=True, key=sort_on)
    return sortedchars