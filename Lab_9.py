#Daniel Duong and Matthew Machado.

def main():
    #Create a list.
    placings = ['United States', 'Sweden', 'Switzerland', 'Canada', 'Great Britain', 'Norway', 'South Korea', 'Japan', 'Italy', 'Denmark']
    country = 'Kirby'

    while country != 'quit':
        country = input('Enter a country that participated in 2018 Winter Olympics or ''quit'': ')

        if country == 'quit':
            print('Exiting')
            break

        for i in range (len(placings)): # Starts with 0
            if country == placings[0]:
                print(country, 'won gold.')
                break

            elif country == placings[1]:
                print(country, 'won silver.')
                break

            elif country == placings[2]:
                print(country, 'won bronze.')
                break


            elif country in placings: # Hint: make a complete thought. Ask if if this is awnserable in a way. True or False. Treated as for in in range ()
                for index in range(len(placings)):
                    if country == placings[index]:
                        print(country, 'placed', index + 1)
                        break

            else:
                print(country, 'did not compete.')    
            break

       
        

main()
        
        
    
