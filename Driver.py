# Evan Johanns
# assignment 12
# 4/21/2020
import re
choice = 0
# should print the menu after every action is made, unless user enters 11
while choice != 11:
    my_string = input("Please type here: ")

    print("Please select an action by typing the number.")
    print(" 1. Does this contain 'q'?")
    print(" 2. Does this contain 'the'?")
    print(" 3. Does this contain a star '*'?")
    print(" 4. Does this contain a digit?")
    print(" 5. Does this contain a period '.'")
    print(" 6. Does this contain two consecutive vowels?")
    print(" 7. Does tihs contain white space?")
    print(" 8. Does this contain have repeated letters in one word?")
    print(" 9. Does this start with 'Hello'?")
    print(" 10. Does this contain an email address?")
    print(" 11. Exit")

    choice = int(input(">>")) # menu input

    if choice == 1: # menu choice 1
        regex = r"\.*[q]\.*" # looking for the letter q
        if re.search(regex, my_string): # if my_string contains q, print true
            print(True)
            print("This contains the letter 'q'.")
        else:
            print(False)
            print("This does not contain the letter 'q'.")

    if choice == 2: # menu choice 2
        regex = r".*[the].*" # looking for the word 'the'
        if re.search(regex, my_string):
            print(True)
            print("This contains the word 'the'.")
        else:
            print(False)
            print("This does not contain the word 'the'.")

    if choice == 3: # menu choice 3
        regex = r".*[\*].*" # looking for the metacharacter '*'
        if re.search(regex, my_string):
            print(True)
            print("This contain the metacharacter star '*'.")
        else:
            print(False)
            print("This does not contain the metacharacter star '*'.")

    if choice == 4: # menu choice 4
        regex = r".*[0-9+].*" # looking for any digits/numbers
        if re.search(regex, my_string):
            print(True)
            print(f"This does contain a digit. The digit(s) was/are {re.search(regex, my_string)}")
        else:
            print(False)
            print("This does not contain a digit.")
    if choice == 5:
        regex = r".*[\.+].*"
        if re.search(regex, my_string):
            print(True)
            print("This contains the character period '.' .")
        else:
            print(False)
            print("This does not contain the character period '.' .")
    if choice == 6:
        regex = r".*[aeiou]{2}.*"
        if re.search(regex, my_string):
            print(True)
            print(f"This contains repeating vowels. they are {re.search(regex, my_string)}")
        else:
            print(False)
    if choice == 7:
        regex = r".*[\s+].*"
        if re.search(regex, my_string):
            print(True)
            print("This contains white space.")
        else:
            print(False)
            print("This does not contain white space")
    if choice == 8:
        regex = r".*[A-Za-z]{2,3}+.*"
        if re.search(regex, my_string):
            print(True)
            print("This contains repeating letters.")
        else:
            print(False)
            print("This does not contain repeating letters.")
    if choice == 9:
        my_string.lower()
        regex = r".*[hello].*"
        if re.search(regex, my_string):
            print(True)
            print("This contains the word 'Hello'.")
        else:
            print(False)
            print("This does not contain the word 'Hello'.")
    if choice == 10:
        regex = r".[@].*\..*"
        if re.search(regex, my_string):
            print(True)
            print("This contains an email address.")
        else:
            print("This does not contain an email address.")







