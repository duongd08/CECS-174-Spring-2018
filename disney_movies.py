def read_disney_movies(file_name):
    result = {}

    first_line = True

    for line in open(file_name):
        if first_line:
            first_line = False
            continue

        split_line = line.split(",")
        result[split_line[1]] = split_line[2] # 1 = actor. 2 = disney movie.

    return result

def main():
    all_disney_movies = read_disney_movies("disney-voice-actors.csv")
    search_for_actor = input("Please enter an actor or quit!: ")

    while search_for_actor != "quit":
        check = True

        for actor in all_disney_movies: #Iterates through a csv.

            if search_for_actor == actor:
                check = False
                print("The actor of {0} is {1}".format(all_disney_movies[actor], actor))

        if check:
            print("{0} is not an actor.".format(search_for_actor))

        search_for_actor = input("Please enter an actor or quit!: ")

                                    
main()
