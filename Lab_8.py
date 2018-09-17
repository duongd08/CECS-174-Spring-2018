#Daniel Duong and Matthew Machado.

#Program will accept all 4 formats.
#Interstate XYZ
#I-XYZ
#IXYZ
#XYZ

def get_interstate_number():
    highway = input('Please enter a US Interstate Highway route number: ')

    if highway[0:11] == 'Interstate ':
        highway_number = highway[11:]
    

    elif highway.startswith('I-'):
        highway_number = highway[2:]
        
        

    elif highway[0] == 'I':
        highway_number = highway[1:]
        

    else:
        highway_number = highway
        

    return int(highway_number)

        
def main():
    highway = get_interstate_number()

    direction = highway % 2

    size = highway % 5

    last_two_digits = highway % 100

    first_digit = highway // 100

    if 0 < highway <= 99:
        if (highway % 2 == 0):
            print('Interstate', highway, 'is a long-distance arterial highway oriented east-west.')

        else:
            print('Interstate', highway, 'is a long-distance arterial highway oriented north-south.')

    if 999 >= highway >= 100:
        if (first_digit % 2 == 0):
            print('Interstate', highway, 'is a circumfirential highway', 'of Interstate', last_two_digits)

        else:
            print('Interstate', highway, 'is a spur highway', 'of Interstate', last_two_digits)

main()

