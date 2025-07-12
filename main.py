import sys
from stats import get_num_words, convert_to_lowercase, sort_list

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def get_num_words(text):
  num_words = len(text.split())
  return num_words

def main():

  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  text = get_book_text(sys.argv[1])
  total_words = get_num_words(text)
  dict_letters = convert_to_lowercase(text)
  sorted_list = sort_list(dict_letters)

  print(f"Found {total_words}")

  for item in sorted_list:
    print(f"{item["char"]}: {item["num"]}")

main()
