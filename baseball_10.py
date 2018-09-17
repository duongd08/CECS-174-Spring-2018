#Daniel Duong and Matthew Machado.

# Write these functions:

# read_players -- returns a list of player tuples
# print_player -- given a player tuple, print that player's information
# find_player -- given a list of players and a name, returns the tuple for the
#   player with the given name
# find_highest_avg -- given a list of players, returns the tuple for the player
#   with the highest batting average (AVG)

def read_players(file_name):
    result = []

    first_line = True
    
    for line in open(file_name):
        if first_line:
            first_line = False
            continue
        
        # read: Name=0, Team=1, AB=3, HR=9
        split_line = line.split(",")
        # strip('"')
        
        player = (split_line[0].strip('"'), split_line[1].strip('"'),\
                  int(split_line[3].strip('"')), int(split_line[9].strip('"')), float(split_line[21].strip('"'))) #Add strip_line[21] to packing, so avg can be read.
        result.append(player)

    return result

def main():
    all_players = read_players("baseball_players.csv")
    choice = 0
    while choice != 5:
        print("1. Search for player")
        print("2. Search for team")
        print("3. Find max homeruns")
        print("4. Find max batting average")
        print("5. Quit")

        choice = int(input("Enter a choice: "))
        if choice == 1:
            search_for_player(all_players)
        elif choice == 2:
            search_for_team(all_players)
        elif choice == 3:
            find_max_hrs(all_players)
        elif choice == 4:
            find_highest_avg(all_players)
        elif choice == 5:
            print("Bye!")

def print_player(player):
    (name, team, ab, hr, avg) = player
    print("{0} ({1}): {2} AB, {3} HR, {4} AVG".format(name, team, ab, hr, avg))

def find_max_hrs(all_players):
     nums = 0 #Starting Player
     maxNum = 0 # Starting Varaible
     for player in all_players:
         (name, team, ab, hr, avg) = player 
         if hr > maxNum: # Updates maximum homeruns as it goes on.
             maxNum = hr
             nums = player
     print_player(nums)

def search_for_team(all_players):
    # Ask the user to type in a team name
    # Iterate through all the players
    # When you find a player on the team that the user input,
    
    search_team = input("Please enter a team name: ")

    for team in all_players:
        (name, team, ab, hr, avg) = team
        if team == search_team:
            print("{0} ({1}): {2} AB, {3} HR, {4} AVG" .format(name, team, ab, hr, avg))

def find_highest_avg(all_players):
    maxNum = 0
    nums = 0 #Starting Player
    qualification = 100 # Starting Varaible
    for player 	in all_players: #Iterates through a list.
         (name, team, ab, hr, avg) = player 
         if ab >= qualification: # Updates maximum homeruns as it goes on.
             if avg > maxNum:
                 maxNum = avg
                 nums = player
    print_player(nums)
            
    
def search_for_player(all_players):
    search_name = input("Please enter a player's name:")

    for player in all_players:
        (name, team, ab, hr, avg) = player
        if name == search_name:
            print_player(player)
            break

#def find_highest_average(all_players):
    
            
main()
