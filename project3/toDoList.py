reponse = input("do you want to add ,view , remove or exit \n")

commands = ["add", "view", "remove", "exit"]
notes = ["zedd", "ab", "azer"]
score = 0
confirmCommand = ""


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
elif reponse == "view":
    print(f'you want to view item {notes}')

else :
    print('------this command not found')

# for command in commands :
#   if command == reponse :
#     print(f'your command is : {reponse} and the {command}')
