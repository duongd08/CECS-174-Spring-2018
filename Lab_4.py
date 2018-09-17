#This lab is done by Daniel Duong and Marlon Molina.

judge_score = -1 #Global Constants.
judge_count  = 0

minimum = 11
maximum = 0
total_score = 0


for judge_count in range(0, 9):
    judge_score = float(input("Enter the judge #{0}'s score:" .format(judge_count + 1)))

    while judge_score < 0 or judge_score > 10: #Validation
        judge_score = float(input("Enter the judge #{0}'s score:" .format(judge_count + 1)))

 
    if judge_score > maximum:
            maximum = judge_score

    if judge_score < minimum:
            minimum = judge_score

    total_score += judge_score
    average_score = (total_score - maximum - minimum) / 7
    
print('The average score is:', average_score)
            
        
        
   
