from screen import clean_screen, return_screen

def open_pc(player):
    clean_screen()
            
    print("-" * 15)
    print("  INVENTARIO")
    print("-" * 15)

    number_pokemon = 0

    print("[0] Voltar")

    for pokemon in player.pokemons:
        number_pokemon = number_pokemon + 1

        print(f"[{number_pokemon}] {pokemon}")

    

    