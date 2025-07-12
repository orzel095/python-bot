def get_num_words(text):
  num_words = len(text.split())
  return num_words

def convert_to_lowercase(text):
  lowercase_text = text.lower()
  unique_letters = {}

  for letter in lowercase_text:
    if letter in unique_letters:
      unique_letters[letter] += 1
    else:
      unique_letters[letter] = 1
  
  return unique_letters

def sort_on(items):
    return items["num"]
  

def sort_list(list):
  arr = []

  for key in list:
    if key.isalpha():
      arr.append({"char": key, "num": list[key]})
  
  arr.sort(reverse=True, key=sort_on)
  return arr  
