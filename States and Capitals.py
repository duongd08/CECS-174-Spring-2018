import random

def main():
  capitals = { "Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix", "Arkansas":"Little Rock", "California":"Sacramento", "Colorado":"Denver", "Connecticut":"Hartford", "Delaware":"Dover", "Florida":"Tallahassee", "Georgia":"Atlanta", "Hawaii":"Honolulu", "Idaho":"Boise", "Illinois":"Springfield", "Indiana":"Indianapolis", "Iowa":"Des Moines", "Kansas":"Topeka", "Kentucky":"Frankfort", "Louisiana":"Baton Rouge", "Maine":"Augusta", "Maryland":"Annapolis", "Massachusetts":"Boston", "Michigan":"Lansing", "Minnesota":"St. Paul", "Mississippi":"Jackson", "Missouri":"Jefferson City", "Montana":"Helena", "Nebraska":"Lincoln", "Nevada":"Carson City", "New Hampshire":"Concord", "New Jersey":"Trenton", "New Mexico":"Santa Fe", "New York":"Albany", "North Carolina":"Raleigh", "North Dakota":"Bismarck", "Ohio":"Columbus", "Oklahoma":"Oklahoma City", "Oregon":"Salem", "Pennsylvania":"Harrisburg", "Rhode Island":"Providence", "South Carolina":"Columbia", "South Dakota":"Pierre", "Tennessee":"Nashville", "Texas":"Austin", "Utah":"Salt Lake City", "Vermont":"Montpelier", "Virginia":"Richmond", "Washington":"Olympia", "West Virginia":"Charleston", "Wisconsin":"Madison", "Wyoming":"Cheyenne" }
  points = 0
  states = []
  print("-States Capital Quiz-")
  for i in range(1,11):
    state = getState(capitals)
    while state in states:
      state = getState(capitals)
    states.append(state)
    randomChoices = randomizeChoices(capitals,state)
    choice = askQuestion(state,randomChoices,i)
    correct = checkCorrect(choice,randomChoices,state,capitals)
    if correct == True:
      points += 1
  print("You got",points,"out of 10 correct")

def getState(capitals):
  listStates = list(capitals.keys())
  randState = listStates[random.randint(0,(len(listStates)-1))]
  return randState

def getIncorrectChoices(capitals):
  listCapitals = list(capitals.values())
  incorrectCapitals = []
  for i in range(3):
    capital = listCapitals[random.randint(0,(len(listCapitals)-1))]
    while capital in incorrectCapitals:
      capital = listCapitals[random.randint(0,(len(listCapitals)-1))]
    incorrectCapitals.append(capital)
  return incorrectCapitals

def randomizeChoices(capitals,state):
  correctAnswer = capitals[state]
  choices = getIncorrectChoices(capitals)
  while correctAnswer in choices:
    choices = getIncorrectChoices(capitals)
  choices.append(correctAnswer)
  random.shuffle(choices)
  return choices

def checkInput():
  validInput = ["A","a","B","b","C","c","D","d"]
  choice = str(input("Enter your choice as a letter:"))
  while choice not in validInput:
    choice = str(input("Invalid input. Enter your choice as a letter:"))
  return choice

def askQuestion(state,randomChoices,i):
  print('')
  print(str(i)+". The capital of", state,"is:")
  print("     a.",randomChoices[0],"b.",randomChoices[1],"c.",randomChoices[2],"d.",randomChoices[3])
  userInput = checkInput()
  if userInput == "a" or userInput == "A":
    choice = randomChoices[0]
  elif userInput == "b" or userInput == "B":
    choice = randomChoices[1]
  elif userInput == "c" or userInput == "C":
    choice = randomChoices[2]
  elif userInput == "d" or userInput == "D":
    choice = randomChoices[3]
  return choice

def checkCorrect(choice,randomChoices,state,capitals):
  if choice == capitals[state]:
    print("Correct!")
    return True
  else:
    print("Incorrect. The correct answer is:", capitals[state])
    return False
main()
