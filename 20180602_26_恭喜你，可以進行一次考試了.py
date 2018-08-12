def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # 15
    """Prints the first word after popping it off."""
    word = words.pop(0) # 1
    print(word) # 2

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # 3
    print(word) # 4

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.") # 16
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') # 17

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print("--------------") # 18
print(poem) # 19
print("--------------") # 20

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five) # 5

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # 6
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # 7 8

print("With a starting point of: %d" % start_point) # 9
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)) # 10

start_point = start_point / 10

print("We can also do that this way:") # 11
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)) # 12 13 14

