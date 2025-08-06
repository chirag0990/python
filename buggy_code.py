# buggy error code

"""def add_underscore(word):
    new_word = "_"
    for char in word:
        new_word = char + "_"
    return new_word

pharse = "hello"
print(add_underscore(pharse)) """   

# solved code

def add_underscore(word):
    new_word = "_"
    for char in word:
        new_word = new_word + char + "_"
    return new_word

pharse = "hello"
print(add_underscore(pharse))