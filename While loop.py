# simple program using while loop and if statements.

command = ""
started = False

while True:
    command= input("> ").lower()
    if command =="start":
        if started:
            print (" The car  already started")
        else:
            started = True
            print("car started...")
    elif command =="stop":
        if not started:
            print("The car already stopped")
        else:
            started = False
            print("car stopped...")
    elif command =="help":
        print(""" 
         start - to start the car
         stop  - to stop the car
         quite - to exit.
          """)
    elif command == "quite":
        break
    else :
        print(" Sorry I don't understand that")