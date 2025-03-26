from stats import *

def get_book_text(path_to_file=None):
    if path_to_file is None:
        raise ValueError("A file path must be provided!")
    file_contents = ""
    with open(path_to_file, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def get_book_text(path_to_file=None):
   if path_to_file is None:
       raise ValueError("A file path must be provided!")
   file_contents = ""
   with open(path_to_file, "r", encoding="utf-8") as f:
       file_contents = f.read()
   return file_contents


def main ():

   print ("============ BOOKBOT ============")
   print (f"Analyzing book found at {book_location}...")
   print ("----------- Word Count ----------")
  
   book = get_book_text (book_location)
   num_words = count_words(book)
   print(f"Found {num_words} total words")
  
   # First, get the dictionary from your function
   char_counts = count_characters(book)


   # Then sort the items
   sorted_chars = sort_characters(char_counts.items())


   # Print with proper string formatting
   for char_dict in sorted_chars:
       char = char_dict["char"]
       count = char_dict["count"]
       print(f"{char}: {count}")

print ("============= END ===============")


import sys
print ("argument list: ", str(sys.argv))
if len(sys.argv) == 1:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_location = sys.argv[1]

main ()


