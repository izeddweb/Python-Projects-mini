
commands = ["add", "view", "remove", "exit"]
notes = ["zedd", "ab", "azer"]
score = 0
confirmCommand = ""

while True :
    reponse = input("do you want to add ,view , remove or exit \n")

    if reponse == "add":
        score += 1
        confirmCommand = input("item to add \n")
        notes.append(f"{confirmCommand}-{score}")
        print(notes)

    elif reponse == "remove":
        confirmCommand = input(" item to remove \n")
        for note in notes:
            if note == confirmCommand:
                notes.remove(note)
                print(f'-{ note} --- {notes}')
            elif note != confirmCommand :
                print('item not found')
    elif reponse == "view":
        for note in notes :
            score += 1  
            print(f' item number{ score } : {note} ')

    elif reponse == "exit" :
        confirmCommand = input(" do you want to exit !! \n")
        if confirmCommand == 'yes':
            print(' OH NOOOO N A K A M A.  !!!!!!')
            break
        else :
            print(' ok N A K A M A')
        
    else :
        print('------this command not found')


