#Daniel Duong and Emmanuel Ramos.

def read_countries(file_name):
    result = {} # Change list into a dictionary

    first_line = True
    
    for line in open(file_name):
        if first_line:
            first_line = False
            continue

        split_line = line.split(",")
        result[split_line[0]] = split_line[1] # 0 = country, 1 = country capital.

    return result
        
            

def main():
    all_countries = read_countries("country-capitals.csv")
    search_for_country = input("Please enter a country name or quit!: ")
    
    while search_for_country != 'quit':
        check = True # In case if there is no dictionary in dictionary.

        for country in all_countries: # Iterates through a csv.

            if search_for_country == country:
                check = False # False since the input is a country.
                print("The capital of {0} is {1}".format(country, all_countries[country]))

        if check: # Non countries go here.
            print("{0} is not a country.". format(search_for_country))

        search_for_country = input("Please enter a country name or quit!: ")




main()
