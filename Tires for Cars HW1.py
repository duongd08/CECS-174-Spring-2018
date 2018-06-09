loop = 1

while loop == 1:
    print("""Main Menu:
    1. Cost of Gas
    2. Used Value
    3. Stopping Distance
    4. CYA Later dawg
    """)

    function = int(input("""Choose a function from the list:
        """))
    
        

#Perameters for Cost of Gas

    if function == 1:
        car_mile1 = float(input("Enter car 1's mileage: "))
        while car_mile1 < 1:
            car_mile1 = float(input("Enter car 1's mileage: "))
        car_mile2 = float(input("Enter car 2's mileage: "))
        while car_mile2 < 1 :
            car_mile2 = float(input("Enter car 2's mileage: "))
        avg_gass1 = float(input("Enter car 1's average gas cost per gallon: "))
        while avg_gass1 < 1:
            avg_gass1 = float(input("Enter car 1's average gas cost per gallon: "))
        avg_gass2 = float(input("Enter car 2's average gas cost per gallon:" ))
        while avg_gass2 < 1:
            avg_gass2 = float(input("Enter car 2's average gas cost per gallon:" ))

        mile_month = float(input("How many miles do you drive a month:"))
        while mile_month < 1:
            mile_month = float(input("How many miles do you drive a month:"))
        mile_year = mile_month * 12

#Calculate Car 1 and Car 2 savings
        total_1cost = (mile_year * avg_gass1) / car_mile1
        total_2cost = (mile_year * avg_gass2) / car_mile2

        if total_1cost > total_2cost:
            car_savings = (total_1cost - total_2cost)
            print('Car 1 will save','${0:.2f}' .format(car_savings) , 'in a year')
        elif total_2cost == total_1cost:
             print('The two cars cost the same')
        else:
            car_savings = (total_2cost - total_1cost)
            print('Car 2 will save','${0:.2f}' .format(car_savings) , 'in a year')

#Perameters for Used Value (Function 2)
        og_price = 0.0
        years = 0.0
        #Decrease .18 a year
    if function == 2:
        og_price = float(input("Enter original car price: "))
        while og_price < 1:
            og_price = float(input("Enter original car price: "))
        years = int(input("Enter number of years: "))
        while years < 1:
            years = int(input("Enter number of years: "))
    #Use range for years 1 to user input
        for years in range(1,years+1):
            new_price =(og_price * float(.18))
            og_price = og_price - new_price
            print('Year {0} value: ${1:.2f}' .format(years,og_price))



#Perameters for Stopping Distance (Function 3)
        initial_speed = 0.0
        tire_cond = 0.0

    if function == 3:
        initial_speed = float(input("Enter initial speed:"))
        while intial_speed < 1:
            initial_speed = float(input("Enter initial speed:"))
        tire_cond = int(input("Enter tire condition ( 1 = new, 2 = good, 3 = poor"))
        while tire_cond <= 0 and tire_cond >= 4:
            tire_cond = int(input("Enter tire condition ( 1 = new, 2 = good, 3 = poor"))
        #Calculation for Stopping Distance
        new_tire = 0.8
        good_tire = 0.6
        poor_tire = 0.5
        FPS = 1.46667
        GRAV = 32.174
        d = (initial_speed * 5280) / (3600)
        if tire_cond == 1: 
            distance = (initial_speed**2) / (2 * new_tire * GRAV)
            print('At',initial_speed,'miles per hour with new tires, the car will stop in','{0:.2f}' .format(d) ,'feet away')
        elif tire_cond == 2:
            distance = (initial_speed**2) / (2 * good_tire * GRAV)
            print('At',initial_speed,'miles per hour with good tires, the car will stop in','{0:.2f}' .format(d) ,'feet away')
        elif tire_cond == 3:
            distance = (initial_speed**2) / (2 * poor_tire * GRAV)
            print('At',initial_speed,'miles per hour with new tires, the car will stop in','{0:.2f}' .format(d) ,'feet away')
#Perameters for Quit
    if function == 4:
        loop = 0
