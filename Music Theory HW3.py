import musicbox

# Name = "D. Duong"

#sharp = #
#flat = b

#whole = 2
#half = 1

#Patterns
#sharp = NOTE_NUMBERS + 1
#flat b = NOTE_NUMBERS - 1

NOTE_LETTERS = ["C", "D", "E", "F", "G", "A", "B"] #Global Constants.
NOTE_NUMBERS = [60, 62, 64, 65, 67, 69, 71]
MAJOR_SCALE_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_SCALE_INTERVALS = [2, 1, 2, 2, 1, 2, 2]
m = musicbox.MusicBox() #Creating a musicbox.

def note_to_int(note):
    #print(note) Print out for testing purposes only.
    if len(note) == 0 or len(note) > 2: # You MUST compare the length of the note before the for loop.
        return -1

    for n in NOTE_LETTERS: # You want to iterate through the list of NOTE_LETTERS.
        if note[0] == n: #Checking for the letter itself, ignoring sharps and flats.
            if len(note) == 1:
                return NOTE_NUMBERS[NOTE_LETTERS.index(n)]

            elif note[1] == "#": # If there is a sharp(#) at index one at any letter, you add 1.
                return NOTE_NUMBERS[NOTE_LETTERS.index(n)] + 1

            elif note[1] == "b": # If there is a flat(b) at index one at any letter, you subtract 1.
                return NOTE_NUMBERS[NOTE_LETTERS.index(n)] - 1

    return -1 # Returns -1 when an invalid letter or unrecognized note is detected.

#print(note_to_int('C#')) #Print out for testing purposes only. To make sure that it works.
#print(note_to_int('A'))
#print(note_to_int('Fb'))
#print(note_to_int('I#'))

def note_to_scale(note, type): #Note represents an integer, while type represents 'major' or 'minor'.
    new_list = [] # Create a new list.

    if type == "major": #Check to determine whether if SCALES is a major or a minor.
        SCALES = MAJOR_SCALE_INTERVALS

    elif type == "minor": #If not major, then it must be minor.
        SCALES = MINOR_SCALE_INTERVALS

    new_list.append(note) #Adds the very first number to the list new_list

    for n in SCALES: #Iterates through every element in the list of MAJOR_SCALE_INTERVALS or MINOR_SCALE_INTERVALS
        note += n   #Adds the additional numbers after the very first number, according to SCALES.
        new_list.append(note)

    #print(new_list) #Test to visualize wheter if it is working or not.

    return new_list

#note_to_scale(60, 'major') #Print out for testing purposes only to make sure if it was returning the correct list for major or minor scale.
#note_to_scale(60, 'minor')


def print_menu(): #Prints out the menu options.
    print("Main Menu:")
    print("1. Play Notes")
    print("2. Play Scale")
    print("3. Quit")

def get_menu_choice(): #Gets user choice and goes from there.
    choice = -1
    while choice < 1 or choice > 3: #Validation occurs when user puts any number that is less than 1 or greater than 3.
        choice = int(input("Please Enter a Selection:"))
    return choice


def get_notes():
    series_of_notes = input("Enter a series of notes seperated by spaces : ")
    sequences = series_of_notes.split(' ') #Splits within a certain character

    tones = []
    for n in sequences: #Iterate through the list of which turned out to be the user input.
        note = note_to_int(n) #Call note_to_int()

        if note > 0: #Makes sure that -1 is not returned in the list. Only returns valid notes if sharp, constant, or flat.
            tones.append(note) #Adds numbers to the list tones.

    return tones

#print(get_notes()) #Test to visualize wheter if it is working or not.

def play_notes(notes):
    era = 500 # Variable for milliseconds
    for n in notes: #You want to iterate through the list of notes, which turned to be series_of_notes (user input), in order to play all sounds.
        m.play_note(n, era)


def menu_play_notes():
    recieving_notes = get_notes() # Call get_notes()

    if len(recieving_notes) == 0: # Results when length of the list is 0.
        print("I don't know any of these notes.")

    elif len(recieving_notes) > 0: # Results when length of list is 1 or greater.
        play_notes(recieving_notes)

def get_scale():
    scale_name = input("Enter a scale name (Ex. C major):") #User input
    new_scale_name = scale_name.split(' ')  #Splits the user input and turns into a list. Also splits the elements into 2 indexes. Ex: Index 0 = C#, Db, or E. Index 1 = 'major' or 'minor'.
    note_letter = new_scale_name[0] # Index 0 = C, D, E, F, G, A, or B
    note_type = new_scale_name[1] # Index 1 = 'major' or 'minor'
    carryover = note_to_int(note_letter) #Calls note_to_int(note) for validation. Returns -1 for any bad letters.


    while note_type != "major" and note_type != "minor" or carryover == -1: #Validation when user input is not equal to a note in the list NOTE_LETTER or when 'major or minor' is spelled incorrectly (MAJOR, MINOR)
        scale_name = input("Enter a scale name (Ex. C major):") # Beware of naming your variables.
        new_scale_name = scale_name.split(' ')  # Splits the user input and turns into a list. Also splits the elements into 2 indexes. Ex: Index 0 = C#, Db, or E. Index 1 = 'major' or 'minor'.
        note_letter = new_scale_name[0]  # Index 0 = C, D, E, F, G, A, or B
        note_type = new_scale_name[1]  # Index 1 = 'major' or 'minor'
        carryover = note_to_int(note_letter)  # Calls note_to_int(note) for validation. Returns -1

    return scale_name

def play_scale(scale):
    era = 500 # Time in milliseconds.
    for n in scale: # Iterates through a list where a scale is given.
        m.play_note(n, era)


def menu_play_scale():
    scales  = get_scale() # Call get_scale
    new_scales = scales.split(' ') # Splits user input into 2 parts and into a list.

    note = new_scales[0]
    conversion = note_to_int(note)

    type = new_scales[1]
    recieving = note_to_scale(conversion, type) # Recieving is a list of music notes, expected from the user.

    #print(recieving) #Printing for testing purposes only.
    scale = recieving
    playing_scales = play_scale(scale)

def main():
    print_menu()
    choice = get_menu_choice()
    while choice != 4: # If choices are not anything less than 4 or greater than 4, the options will appear.

        if choice == 1: # Option # 1
            menu = menu_play_notes()
            print_menu()
            choice = get_menu_choice()

        elif choice == 2: # Option # 2
            menu2 = menu_play_scale()
            print_menu()
            choice = get_menu_choice()

        elif choice == 3: # Option # 3
            print("Bye!")
            break

    m.close()

main()
