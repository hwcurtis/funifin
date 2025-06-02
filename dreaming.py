print ("""You have awoken out in the cold darkness, unsure how you came to be here, all of a sudden you
hear a noise behind you , you see three options, one hiding in the bush on the left, going straight into the unkown, or taking your chances and going right , what will you choose?""")
choice = input("type right, left or straight: ")
if choice == "right":
     print ("you choose to go right and see a small stream , which by chance has a nearby jug")
     print ("you pick up the jug and fill it with water, you are now hydrated")
elif choice == "left":
    print("You chose the left path and found a bush. Do you want to pick up a stick or wait?")
    choice2 = input("type stick or wait: ")
    if choice2 == "stick":
        print("You chose a stick. Do you want to attack or wait?")
        choice3 = input("type attack or wait: ")
        if choice3 == "attack":
            print("Be sure you're ready for whatever you encounter.")
            print("You throw the stick and run away.")
        elif choice3 == "wait":
            print("You decided to wait. Something might happen soon.")
        else:
            print("Invalid choice. The adventure ends here.")
    elif choice2 == "wait":
        print("You decided to wait by the bush. Something might happen soon.")
# (Removed redundant commented-out code for clarity)
    #else:
    #    print("Invalid choice. The adventure ends here.")
#else:
   # print("You chose something else. Let's move on.")


#choice = input("type pick up the rock or leash: ")
#if choice == "rock":
   # print("You picked up the rock. Prepare to defend yourself!")
    #print("You can throw it or use it as a weapon.")
#elif choice == "leash":
 #   print("Hope that the noise does not come from a big animal.")
  #  print("Your kindness paid off, and it's a puppy!")
# (You can add more choices here for further adventure steps)