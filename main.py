print("hello welcome to the jungle survive if you can.")

print()

def  choice (health ,damage):
  print ("you have", health, "HP")
  print("you do " , damage,"to the enemies")
  print ("----------------")
  
  direction = input("pick a direction,r, l, u, d ")

  if (direction == "r") :                   
    print("you went into a cave and see a unicorn thats actually a t rex ", damage ," damage to t,rex ")
    print ("the t rex dies")
    choice ( 10 , 1 )
  elif (direction == "u"):
    print("you go to another cave ",damage,"and see a sleeping bear")
    print ("you step on a stick and you are worried but you get of the cave safe")
    choice (90,60)
  elif (direction == "l"):
    print("you encountered a dragon do ",damage," damage to the dragon")
    print ("the dragon dies")
    choice (40,60)
  elif (direction == "d"):
    print("you encountered a gorrila  ",damage," damage to the gorrila")
    print ("the gorrilla eats a banana") 
    choice (50,60)
  elif (direction == "d"):
    print("you encountered a evil wizard ",damage,"to the wizard")
    print ("the wizard dies")
    choice (50,60)
  else:
    print ("please put a valid choice r, l, u, d ")
    choice (100,50)

choice(100,50)