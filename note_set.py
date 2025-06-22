from os import system
from time import sleep

def clear():
    system('clear')

def pront(str):
    for letter in str:
        print(letter, end="", flush=True)
        sleep(0.04)

def prant(str):
    for letter in str:
        print(letter, end="", flush=True)
        sleep(0.07)

def quit():
    clear()
    pront('Thank you for using this code!')
    sleep(3)
    clear()
    exit(0)

def opening():
    clear()
    prant('This in note setter.\n')
    prant('the purpose of this code is to edit a note that your input in.\n')
    prant('for number 2 and 3, you can Ctrl+C to get out of the menu.Two options will be there.\n')
    prant("you can't type anything else except number on this code. Or else, it'll result an error.\n")
    prant('enjoy the code!\n')
    sleep(2)
    main()


def main():
    clear()
    pront("I'm a note setter!\n")
    sleep(0.7)
    pront("\n1. Note maker\n2. Note line adder\n3. Note reset to a new line" \
    "\n4. Advanced note editor(Nano)\n5. What is note setter?\n6. Quit")
    sleep(0.09)
    pront("\nJust choose what you want:")
    user = int(input())
    sleep(0.7)
    if user == 1:
        clear()
        pront('Choose a name for the note: ')
        user_note_make = input()
        system(f"touch {user_note_make}")
        sleep(2)
        pront("\nYour note has been made!.\nWould you like to go to the main menu?[Y/n]: ")
        user_mainmenu_make = input().lower()
        if user_mainmenu_make == 'y':
            main()
        else:
            quit()
    elif user == 2:
        clear()
        pront('Input your note filename[Do not get the name wrong!]:')
        user_note_add = input()
        with open(f"{user_note_add}", 'a') as fila:
            clear()
            while True:
                try:
                    pront('\nAdd a line to the note: ')
                    user_note_add_line = input()
                    fila.write(user_note_add_line+'\n')
                except KeyboardInterrupt:
                    fila.close()
                    pront("\nYou're done?[Y/n]: ")
                    user_note_add_quit = input().lower()
                    if user_note_add_quit == 'n':
                        continue
                    else:
                        quit()
                        break
    elif user == 3:
        clear()
        pront('Input your note filename[Do not get the name wrong!]:')
        user_note_reset = input()
        with open(f'{user_note_reset}', 'w') as file:
            clear()
            while True:
                try:
                    pront('\nAdd a line to the note: ')
                    user_note_add_reset = input()
                    file.write(user_note_add_reset+'\n')
                except KeyboardInterrupt:
                    file.close()
                    pront("\nYou're done?[Y/n]: ")
                    user_note_reset_quit = input().lower()
                    if user_note_reset_quit == 'n':
                        continue
                    else:
                        quit()
                        break
    elif user == 4:
        clear()
        pront('Input your note filename[Do not get the name wrong!]:')
        user_nano = input()
        sleep(2)
        system(f'nano {user_nano}')
    elif user == 5:
        opening()
    elif user == 6:
        quit()
    else:
        pront("\nYour choice is invalid!")
        sleep(1)
        main()

if __name__ == "__main__":
    main()