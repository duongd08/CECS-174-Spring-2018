print("Uboats are patrolling the waters")
print("We have to destroy them before they sink more vessels.")
Join = input("Are you up for the task captain?")
if Join == "Yes":
  print("Too determine their position, we have to try and intercept a coded message.")
  Encryption = {"a":"t","b":5,"c":"k","d":8,"e": 6,"f":"d","g":"r","h":".","i":"q","j":"u","k":0,"l":1,"m":"b","n":9,"o":2,"p":4,"q":"s","r":3,"s":7,"t":"n","u":"j","v":"c","w":"i","x":"a","y":"z","z":"o", " ":" "}
  print("Here is an encryption code")
  print(Encryption)
  Intercept = input("Every few seconds a message will come through, try and intercept it")
  Intercept = "Intercept"
  intercepting = True
  
  while intercepting:
    if Intercept == "Intercept":
      print("message intercepted")
      intercepting = False
      story = "approaching lusitania flying the british flag "

      encrpted_msg =''
      for char in story: 
        encrpted_msg=encrpted_msg+ str(Encryption[char])
      print(encrpted_msg)
 
      Decryptedmessage = input("Decrypt this message and enter the name of the boat being targeted")
      if Decryptedmessage == "lusitania":
        print("You have found him")
        number = [4,2,1,7,0,10,9,8]
        index = 0
        for i in range(1,len(number)):
          if number[index] > number[i]:
            index = i
            
        shotarea = int(input("Shoot a location"))
        if shotarea == number[index]: 
          print("You hit them sir.")
        else:
          print("We've been hit, we're going down.")
      
          
              
            
        

      else:
        print("You have not decoded")
        
    else:
     print("Try again")
else:
  print("Have a nice day then.")

