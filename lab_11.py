#Daniel Duong and Matthew Machado.

def main():
    placings = {'Team Liquid' : (1, 100000), # Initialize a dictionary.
                '100 Thieves' : (2, 50000),
                'Echo Fox' : (3, 30000),
                'Clutch Gaming' : (4, 20000),
                'Cloud 9' : (5, 0),
                'Team SoloMid' : (6, 0)}

    team_name_selection = 'Kirby' # Fake Input
    

    while team_name_selection != 'quit': # Beware of identation!
        team_name_selection = input('Enter a team name or "quit"!: ')    

        while team_name_selection not in placings and team_name_selection != 'quit':
            team_name_selection = input('Enter a team name or "quit"!: ')


        if not team_name_selection == 'quit':
            (place, prize) = placings[team_name_selection] # Unpacking.

            if prize > 0:
                print("{0} placed {1} (${2})".format(team_name_selection, place, prize))

            else:
                print(team_name_selection,  "placed ", place)


        if team_name_selection == 'quit': # Be careful of spelling.
            print("Bye!")

main()
