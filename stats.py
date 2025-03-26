def count_words(book):
    return len(book.split())

def count_characters (book):
    lower = book.lower()

    alpha_dict = {}
    for b in lower:
        alpha_dict[b] = alpha_dict.get(b,0) + 1
    return alpha_dict

def sort_characters(char_items):
    char_list = []
    for char, count in char_items:
        if char.isalpha():  # Check if the character is alphabetic
            # Add a dictionary with 'char' and 'count' keys
            char_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list