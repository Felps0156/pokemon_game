import os

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def return_screen():
    print("\nAperte ENTER para voltar")
    input("> ")