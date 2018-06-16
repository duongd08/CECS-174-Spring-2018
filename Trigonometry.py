def main():
    import math
    trig = input('Do you want to calculate sine, cosecant, cosine, secant, tangent, or cotangent?:')

    if trig == 'sine' or trig == 'sin':
        a = eval(input('What is the angle measure?:'))
        result = math.sin(math.radians(a))
        print('The answer is ' + str(round(result, 3)))
        main()

    elif trig == 'cosecant' or trig == 'csc':
        a = eval(input('What is the angle measure?:'))
        result = 1 / math.sin(math.radians(a))
        print('The awswer is ' + str(round(result, 3)))
        main()

    elif trig == 'cosine' or trig == 'cos':
        a = eval(input('What is the angle measure?:'))
        result = math.cos(math.radians(a))
        print('The answer is ' + str(round(result, 3)))
        main()

    elif trig == 'secant' or trig == 'sec':
        a = eval(input('What is the angle measure?:'))
        result = 1 / math.cos(math.radians(a))
        print('The answer is ' + str(round(result, 3)))
        main()
    

    elif trig == 'tangent' or trig == 'tan':
        a = eval(input('What is the angle measure?:'))
        result = math.tan(math.radians(a))
        print('The answer is ' + str(round(result, 3)))
        main()

    elif trig == 'cotangent' or trig == 'cot':
        a = eval(input('What is the angle measure?:'))
        result = 1 / math.tan(math.radians(a))
        print('The answer is ' + str(round(result, 3)))
        main()


    else:
        print('I do not understand what on earth is happening?!')
        main()

main()

