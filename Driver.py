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
        find = my_string
        if find == re.findall(r'\w[q]\w',my_string):
            print(True)
            print("This contains 'q'.")
        else:
            print(False)
            print("This does not contain 'q'.")


    elif choice == 2: # menu choice 2

    elif chioce == 3: # menu choice 3

    elif choice == 4: # menu choice 4

    elif choice == 5: # menu choice 5

    elif choice == 6: # menu choice 6

    elif choice == 7: # menu choice 7

    elif choice == 8: # menu choice 8

    elif choice == 9: # menu choice 9

    elif choice == 10: # menu choice 10

