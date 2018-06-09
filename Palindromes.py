
def print_menu(): #Begin by printing out a menu
    print("""Main Menu:
    1. Is it a palindrome?
    2. Make a palindrome!
    3. Quit
    """)

def get_menu_choice(): 
    choice = int(input('Choose a function from the menu: ')) #Option for user to pick from menu
    
    while choice < 1 or choice > 3: #Validating that input is between 1 and 3, 
        choice = int(input(" Please choose a number from the menu:"))
    return choice

def get_phrase():
    phrase = input('Please input an English phrase: ')

    while phrase != phrase or phrase.isspace(): #Validating user input is string
        phrase = input('Please input an English phrase:')
    return phrase

def is_palindrome(phrase):
    phrase = phrase.lower() #Make letters lowercase, to compare
    i = 0
    j = len(phrase) -1

    while phrase[j].isalpha() == False: #Test if each character is a letter, skips if is not
        j -= 1
    while phrase[i].isalpha() == False: #Test character is letter again
        i += 1

    while i < len(phrase) // 2:
        j = len(phrase) - i - 1

        if phrase[i] != phrase[j]:
            return False
        i += 1
        j -= 1
    return True


def menu_check_palindrome():
    phrase = get_phrase() #Calls functions
    is_palindrome(phrase) #Calls functions

    if is_palindrome(phrase) == True:
        print(phrase,'is a palindrome')
    if is_palindrome(phrase) == False:
        print(phrase,'is not a palindrome')
        
        
def make_palindrome(phrase,skip_last):
    term = "" #Create variable to use for string value
    if skip_last is True:
        for i in range(len(phrase)-1,-1,-1):
            term += phrase[i]
    else:
        for i in range(len(phrase)-2,-1,-1):
            term += phrase[i]
    return phrase + term

def get_repeat_last():
    user_repeat = input('Should the last letter be repeated?("y" or "n"): ') #Ask user input for letter repeat
    while user_repeat != "y" and user_repeat != "n": #Checks that user input is "y" or "n"
        user_repeat = input('Should the last letter be repeated?("y" or "n"): ')
        if user_repeat == "y":
            return True
        elif user_repeat == "n":
            return False
    if user_repeat == "y":
        return True
    if user_repeat == "n":
        return False

def menu_make_palindrome():
    phrase = get_phrase() #Call following functions
    skip_last = get_repeat_last()
    make_palindrome(phrase, skip_last)
    print('"',phrase,'" made into a palindrome is "',make_palindrome(phrase,skip_last),'"')
    

def main():
    loop = 1 #Create loop, that runs until loop value is altered
    while loop == 1:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            menu_check_palindrome()
        elif choice == 2:
            menu_make_palindrome()
        elif choice == 3:
            print("Bye!")
            break #Breaks the loop of the main function
main()


