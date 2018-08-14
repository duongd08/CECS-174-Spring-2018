#A World that's Not Home
#Interactive Fiction Project
#Daniel Duong, Peter Vu
#Alex Nguyen, Cindy Nguyen
#Raul Dieta

import time
#Beginning
print ("...") #time passing
time.sleep(1)
print ("<<CONNECTING...>>") #device connecting 
time.sleep(2)
print ("<<DEVICE_CONNECTED>>") 
time.sleep(2)
print ("...")
time.sleep(2)
print ("Hello?")
time.sleep(1)
print ("Who is this?")
time.sleep(1)
global name #once player types in name, the name will periodically appear 
name = input("(type in your name):")

#Introduction
print ("Hi " + name + "! I'm Henry.") #fills in the blank
time.sleep(1)
print ("Sorry for bothering you, but I'm a little lost.")
time.sleep(2)
#Character explains the situation
print ("I woke up in some kind of bedroom but it's looks really run down and none of the light switches are working.")
time.sleep(3)
print ("I don't remember how I got here and all I have is this device that I'm using to message you right now.") #connects to the player 
time.sleep(3)
print ("I wish this was just some bad dream and once I wake up, I'd be back home smelling Mom's homemade waffles")
time.sleep(3)
print ("There's only one door that leads to outside the building but I'm a little scared to go outside.")
time.sleep(2)
#First decision
print ("What do you think I should do " + name + "? Should I look around the room first or just go outside?")
time.sleep(1)
answer = input('(type "look around" or "go outside"):')
global battery
if answer == "look around":
  battery = 2 #Changes the battery value to less than 1 for the next if statement
  #Goes to check out the house
  print ("Yeah good idea. Maybe I'll find something useful.")
  time.sleep(2)
  print ("...")
  time.sleep(2)
  print ("I wonder who used to live here. How long ago did they leave?")
  time.sleep(2)
  print ("Oh!")
  time.sleep(1)
  print ("I found this battery that doesn't look used. I should keep this just incase.")
  time.sleep(2)
  #Skip checking the room
elif answer== "go outside":
  battery = 0 #Changes the battery value to less than 1 for the next if statement

#Next scene outside
print ("Ok, lets go outside now. There's no point in staying in this house forever.")
time.sleep(2)
print ("...")
time.sleep(2)
print ("Wow... its dark out here too. I must be far from home. There's no sun or moon at all... Just stars...") 
time.sleep(4)
print ("I see something! There's a red blinking light couple yards from here. I'm gonna go check out what it is.")
time.sleep(2)
print ("...")
time.sleep(2)
print ("Cool! It's a robot on the floor, but it's turned off and the words 'LOW BATTERY' are flashing on its face.")
time.sleep(3)
print ("Lets get the robot a new a battery to wake it up. Maybe it could help me figure out how to get home.")
time.sleep(3)
if battery < 1: 
  print ("Sigh... I don't have any batteries with me right now. Maybe there was one in the house. I'm gonna go back and look.") #look for battery 
  time.sleep(2)
  print ("...")
  time.sleep(2)
  print ("Nice! I found a brand new battery in the bedroom on a bookshelf. Lets go back and fix that robot") #uses item 
  time.sleep(2)
  print ("...")
  time.sleep(2)
else:
  print ("I think the one we found in the house might work. Let me replace the robot's old one.")
  time.sleep(2)
  print ("...")
  time.sleep(2)

#After the battery is put in the robot
print ("Yes! It's turning on!")
time.sleep(1)
print ("What's this? It's making weird noises at me. I think it's trying to say something.")
time.sleep(2)
print ("I don't know how to get it to speak properly. Hey " + name + ", it's screen is saying 'ENTER WIRELESS DEVICE CODE'.") 
time.sleep(2)
print ("It also has a short cable attached to its arm. Do you know what I should do with these?")
time.sleep(1)
answer = input("(type 'put in our device code' or 'connect the cable to your device'):") #make a decision 
if answer == "put in our device code": 
  print ("Yeah " + name + ", that's a great idea! But my device doesn't show any code... Does yours say anything?")
  time.sleep(1)
  answer = input("(guess the 3 number code [hint: why was 6 afraid of 7?])") #player puts in the code 
  while answer != "789":
    answer = input("Whoops. I don't think that's the right code. Try again.")
  if answer == "789":
    print ("Awesome! It worked! Thanks " + name + "!")
    time.sleep(2)
    print ("You're so reliable. Just like my big brother!") 
    time.sleep(3)
    print ("... I really miss my family back home... Anyway, let's see if this robot can help us!")
    time.sleep(3)

time.sleep(1)
print ("<<CONNECTING_TO_FEEBO...>>")
time.sleep(2)
print ("FEEBO: HELLO. MY NAME IS FEEBO. WELCOME TO Andromeda, HOW CAN I HELP YOU?") #robot speaking
time.sleep(3)
print ("Wow cool! He's talking through the device! I guess this world's called Andromeda, huh?")
time.sleep(3)
print ("Hey " + name + ", What should we ask FEEBO?" )
time.sleep(1)
answer = input("(type 'what time is it', 'what happened to you', and 'how can henry go home')") #player must ask all questions 
while answer != "how can henry go home": 
  if answer == "what time is it":
    print ("FEEBO: IT IS CURRENTLY 10:06 P.M.") #player recieves answers 
  elif answer == "what happened to you":
    print ("FEEBO: OUR WORLD IS POWERED BY A GENERATOR GIVING ENERGY TO ALL ROBOTS.")
    time.sleep(2)
    print ("FEEBO: UNFORTUNALTELY, IT HAD STOPPED WORKING AND NO ROBOT HAS BEEN ABLE TO TURN IT ON.")
    time.sleep(2)
    print ("Thats sad... without the generator the robots must've been dying off one by one.") #no generator means that the robots going to die 
    time.sleep(2)
    print ("I wish we could help them.")
  time.sleep(1)
  answer = input("FEEBO: WHAT ELSE DO YOU WANT TO KNOW?")
  time.sleep(1)
if answer == "how can henry go home":
 print ("FEEBO: IN ORDER FOR HENRY TO GO HOME, HE WILL HAVE TO GO TO THE TOWER ON THE OTHER SIDE OF THE CANYON.")
 time.sleep(2)
 print ("What's in the tower?")
 time.sleep(2)
 print ("FEEBO: LOCATED IN THE TOWER IS THE GENERATOR THAT POWERS OUR WORLD AND A PORTAL TO YOUR HOME. UNFORTUNATELY, NONE OF THEM HAVE BEEN WORKING IN THE PAST 10 YEARS.")
 time.sleep(3)
 print ("FEEBO: BUT, I BELIEVE YOU, HENRY, MAY BE ABLE TO FIND A WAY TO TURN THEM ON IF YOU GO TO THE TOWER.")
 time.sleep(2)
 print ("Really! So that means I can save you guys and get to go home! Did you here that, " + name + "? FEEBO, how can I get there?") #robot helps boy find a way home 
 time.sleep(3)
 print ("FEEBO: THERE ARE 2 WAYS TO REACH THE GENERATOR'S TOWER. THE FIRST WAY IS ACROSS THE BRIDGE THAT IS LEFT OF HERE AND THE SECOND WAY IS A PATH DOWN THE CANYON INTO A CAVE.") #choose bridge or Canyon
 time.sleep(3)
print ("What do you think I should do " + name + "? Should I go left or right?") #makes the 3rd decision 
time.sleep(1)
answer = input ("type 'left' or 'right': ") #choose left or right
if answer == "left": 
  print ("Ok " + name + ", lets cross the bridge then. Man, I'm afraid of heights.")
  time.sleep(2)
  print ("...")
  time.sleep(2)
  print ("... Whew... I crossed the bridge. Oh whoa, theres a forest on this side of the canyon. But, all the tree's are dead. Is it because Andromeda doesn't have a sun?")
  time.sleep(4)
  print ("I miss having picnics on sunny days with my family... Let's hurry to the tower.")
  time.sleep(3)
  print ("Huh? I see another like in the forest except this time its yellowish. Maybe there's someone else there.")
  time.sleep(2)
  print ("I see a robot! It doesn't look like it's out of battery like FEEBO, but its not moving very smoothly") #new robot 
  time.sleep(2)
  print ("Wow! It has a tree sapling planted that's alive! I guess not every tree has died off yet.")
  time.sleep(2)
  print ("It doesn't have a cable to connect to our device this time so lets use its wireless connection. I'll put in the code.") 
  time.sleep(4)
  print ("Uh-oh, " + name + ". The last code isn't working anymore. Maybe we need another one?")
  time.sleep(1)
  answer = input("(guess the 3 number code [hint: how many dalmations?])") #use the hint to find the code
  while answer != "101":
    answer = input("Nope. I don't think that's the right code. Try again.")
  if answer == "101":
    print ("Perfect! It worked! Thank you, " + name + "!")
  time.sleep(1)
  print ("<<CONNECTING_TO_REEBO...>>")
  time.sleep(2)
  print ("REEBO: HELLO AND NICE TO MEET YOU. I'M SORRY BUT I AM QUITE OCCUPIED RIGHT NOW")
  time.sleep(2)
  print ("What are you doing?")
  time.sleep(2)
  print ("REEBO: THIS IS THE LAST LIVING SAPLING IN THIS FOREST AND I'VE BEEN GIVING LIGHT FOR THIS PLANT TO GROW USING THE YELLOW CRYSTALS FROM THE MINES AT THE BOTTOM OF THE CANYON.") 
  time.sleep(4)
  print ("REEBO: AFTER THE GENERATOR STOPPED, I HAD COME HERE EVERYDAY TO TRY TO SAVE THE FOREST") #forest is dyin
  time.sleep(3)
  print ("REEBO: UNFORTUNATELY, I'M AFRAID I DON'T HAVE MUCH TIME LEFT IN MY LIFE SINCE I WAS NOT BUILT TO USE BATTERIES.")
  time.sleep(3)
  print ("Don't worry! My friend " + name + " and I are going to the generator's tower to save Andromeda. Please hang on until then. Let's hurry " + name + ".")
  time.sleep(4)
if answer ==  ('right'):  
  print ("I see a pathway down the canyon and I found a cave!") #canyon 
  time.sleep(2)
  print ("But... I see another robot depleted of its power. I feel so bad for it... Let's go through the cave fast so we can turn on the generator and save Andromeda.") 
  time.sleep(3)
  print ("Wow, this cave looks like a mine... Woah! There's a bunch of glowing yellow crystals in here! So pretty!") #cave scene 
  time.sleep(2)
  print ("I need to get one of these. My dad and I love collection crystals and gems... I really miss him.")
  time.sleep(3)
  print ("Ok, I'm gonna take one so I can give it to my dad once I go home. I'm gonna keep going now.")
time.sleep(2)
print ("...")
time.sleep(2)
print ("I'm here! I see the tower with the generator! I'm going inside!") #scene takes place in the generator 
time.sleep(2)
print ("I see it! There's the generator and right next to it is what looks like a door! That must be the portal!")
time.sleep(2)
print ("Now... lets find out how to turn them on.")
time.sleep(2)
print ("...")
time.sleep(2)
print ("...")
time.sleep(2)
print ("MESSAGE SENDING...")
time.sleep(4)
print ("Huh? " + name + ", do see this? What's this 'Message'?")
time.sleep(2)
print ("<<CONNECTING_TO_ZEEBO...>>")
time.sleep(2)
print ("ZEEBO: HELLO HENRY AND TO YOUR FRIEND. I AM ZEEBO, THE FIRST ROBOT WHO CAME TO Andromeda.") #new robot in scene 
time.sleep(2)
print (" Woah " + name + ", how did he connect to our devices without a code?")
time.sleep(2)
print ("ZEEBO: HENRY, I HAVE ILL NEWS FOR YOU. IN ORDER TO CHARGE UP THE GENERATOR OR THE PORTAL, YOU MUST PLUG IN YOUR DEVICE INTO ONE OF THE MACHINES.")
time.sleep(3)
print ('Wait ZEEBO, what do you mean by "one of the machines"?')
time.sleep(2)
print ("ZEEBO: HENRY, I'M SORRY TO SAY, BUT YOUR DEVICE ONLY HAS ENOUGH POWER TO START UP ONLY ONE OF THE MACHINES. IF YOU WISH TO START UP ONE, YOUR DEVICE WILL SHUT OFF FOREVER AND YOU WILL NEVER BE ABLE TO USE THE OTHER MACHINE.") #device can only be used once 
time.sleep(4)
print ("... No... It can't be true... so you're saying that if I start up the generator and save all the robots of Andromeda, I'll never be able to talk to " + name + " or go home again?") #final DECISION
time.sleep(4)
print ("ZEEBO: I'M AFRAID SO. BUT, IT IS NOT MY POWER TO TELL YOU WHAT YOU SHOULD DO. YOU MUST MAKE THE CHOICE YOURSELF.")
time.sleep(3)
print ("But... you all don't deserve to just disappear. It's not right.") #the boy must choose either to save the robots or go home 
time.sleep(2)
print ("ZEEBO: WE ROBOTS WILL HAPPILY OBLIGE TO WHATEVER DECISION YOU MAKE. HENRY, THE CHOICE IS YOURS.")
time.sleep(2)
print (name + " I can't decide... I don't want to leave these robots to die but I really miss my family, my home. Help me. Plus, whatever decision I make, I'll never be able to talk to you again... What do you think is the right choice?") #player chooses the last decision
time.sleep(6)
answer = input("(type 'save andromeda' or 'go home'):")
if answer == "save andromeda":
  time.sleep(2)
  print ("Ok... I trust you " + name + ", so I think I should stay too.")
  time.sleep(2)
  print ("Thank you for everything you've done for me " + name + ". You are the best friend in the whole entire world. Without, you I would have been lost forever. So... thank you.") 
  time.sleep(5)
  print ("Ok ZEEBO, I'm turning on the generator.")
elif answer == "go home":
  print ("Ok... I trust you " + name + ", and I really miss home too. So... I'll go home...")
  time.sleep(2)
  print ("Thank you for everything you've done for me " + name + ". You are the best friend in the whole entire world. Without, you I would have been lost forever. So... thank you.")
  time.sleep(5)
  print ("ZEEBO: YOU MADE A DIFFICULT CHOICE, HENRY. BUT I AM HAPPY THAT YOU WILL RETURN TO YOUR FAMILY.") #goes home, means that all robots will die 
  time.sleep(3)
  print ("Please tell FEEBO and REEBO I'm sorry for breaking my promise ZEEBO. Ok. I'm turning on the portal.") #henry will now make a CONNECTION 
time.sleep(2)
print ("...") #time passing 
time.sleep(2)
print ("...")
time.sleep(2)
print ("...") 
time.sleep(2)
print ("<<ATTEMPTING_TO_RECONNECT...>>")
time.sleep(2)
print ("<<ATTEMPTING_TO_RECONNECT...>>")
time.sleep(2)
print ("<<CONNECTION_LOST>>") 
print ("(end)")
#end
