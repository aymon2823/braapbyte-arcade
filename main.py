import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(r"""
 ____                     _           _           
|  _ \ _ __ __ _  ___ ___| |__   __ _| |_   _ ___ 
| |_) | '__/ _` |/ __/ _ \ '_ \ / _` | | | | / __|
|  __/| | | (_| | (_|  __/ |_) | (_| | | |_| \__ \
|_|   |_|  \__,_|\___\___|_.__/ \__,_|_|\__,_|___/

         🏍️  BRAAPBYTE ARCADE CLI  🛠️
    """)

def menu():
    print("""
[1] 🧠 Dirtbike Cyber Quiz
[2] 🎲 Number Guesser
[3] ✊ Rock Paper Scissors
[4] ❌ Exit
""")

def load_game(option):
    clear()
    if option == "1":
        os.system(f'{sys.executable} quiz_game.py')
    elif option == "2":
        os.system(f'{sys.executable} number_guesser.py')
    elif option == "3":
        os.system(f'{sys.executable} rock_paper_scissors.py')
    elif option == "4":
        print("Later skater! 🏁")
        sys.exit()
    else:
        print("Invalid choice. Try again.")
        time.sleep(1)

if __name__ == "__main__":
    while True:
        clear()
        banner()
        menu()
        choice = input("Select your challenge: ")
        load_game(choice)
        input("\nPress Enter to return to the BraapByte menu...")