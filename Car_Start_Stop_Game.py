command = ""
started = False
stopped = False
while True:
    command = input('Your Command: ').lower()
    if command == 'start':
        if started:
            print('Car already started')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started:
            print('Car already stopped')
        else:
            started = False
            print('Car stopped...')
    elif command == 'help':
        print("""
        To start the car...type start
        To stop the car...type stop
        To quit the game...type quit""")
    elif command == 'quit':
        print('You quit the game')
        break
    else:
        print('We did not understand your command...try again or type help for more information')


# OR


"""
command = ""
started = False

while command != "quit":
    command = input("Your Command: ").lower()
    if command == "start":
        if started:
            print("Engine already started")
        else:
            print("Engine Started")
        started = True
    elif command == "stop":
        if not started:
            print("Engine already stopped")
        else:
            print("Engine stopped")
        started = False
    elif command == "quit":
        print("You quit the game")
    else:
        print("Invalid Command")
        
"""