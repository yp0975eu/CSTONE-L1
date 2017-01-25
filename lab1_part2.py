# Write a program that turns a sentence into camel case.
# The first word is lowercase, the rest of the words have their initial letter capitalized,
#  and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER",
# your program will output "fontProcessorAndParser".

# Optional extra question: print a warning message if the input will not produce a valid Python variable name.
#  You don't need to be exhaustive in checking, but test for a few common issues,
# such as starting with a number, or containing invalid characters such as # or + or ".

# Test your program, and comment your code.


def display_banner():
    message = "Awesome Camel Case Program"

    stars = '*' * len(message)

    print('\n', stars, '\n', message, '\n', stars, '\n')


def camel_case_sentence(sentence):
    # lowercase all letters
    l_sentence = sentence.lower()

    # split sentence into words,
    words = l_sentence.split(' ')

    # flag for skipping first word
    first_word = True

    # new list of words
    new_list = []

    # loop through list and uppercase first letter, except for the first word
    for word in words:
        # skip first word
        if first_word:

            first_word = False

            new_list.append(word)

            continue

        new_list.append(word.capitalize())

    # https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    # collapse list into string
    return ''.join(new_list)

    # reassemble sentence with capitals on first letters, except first word


def test_if_valid_python_variable(variable):
    # cannot start with number
    # cannot contain punctuation characters
    # cannot be reserved word

    # checks if contains any punctuation, or numbers
    for letter in variable:
        if not letter.isalpha():
            return False

    return True

if __name__ == '__main__':

    display_banner()

    # prompt user for sentence

    sentence = input("Enter a sentence to turn it into camel case:\n")
    # test_sentence = " he QuiCk bRown FoX Jumped Over the LaZY Dog"

    # convert to camel case
    variable = camel_case_sentence(sentence)

    # if it is valid, print variable
    if test_if_valid_python_variable(variable):

        print(camel_case_sentence(sentence))

    # if not valid, print error message
    else:
        print("not valid variable")
