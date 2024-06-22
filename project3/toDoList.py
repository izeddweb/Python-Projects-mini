commands = ["add", "view", "remove", "exit"]
notes = ["zedd", "a"]
score_Note = 0
confirmCommand = ""

while True:

    user_command = input(" Choose a commands from (add ,view , remove ,exit) : ")
    if user_command == "add":
        confirmCommand = input("item to add : ")
        notes.append(confirmCommand)
        print(f" item added : ", notes)

    elif user_command == "view":
        if len(notes) == 0:
            print("no item to view")
        else:
            print(notes)

    elif user_command == "remove":
        print(notes)
        confirmCommand = input("item to remove! :")
        for note in notes:
            if confirmCommand == note:
                for note in notes:
                    notes.remove(confirmCommand)
                    print(f" item removed from you list {notes} ")
                    break
            else:
                confirmDelete = input("this item not found you want to add ? ")
                if confirmDelete == "yes":
                    notes.append(confirmCommand)
                    print(f" item added : ", notes)
                    break
                else:
                    print("   it's a joke ")
                    break

    elif user_command == "exit":
        confirmCommand = input("you want to exit !! : ")
        if confirmCommand == "yes":
            break
        else:
            print(" welcome back")
    else:
        print(" command not found!")
