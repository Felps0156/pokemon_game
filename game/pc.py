from screen import clean_screen, return_screen

def open_pc(player):
    clean_screen()
            
    print("-" * 15)
    print("  INVENTARIO")
    print("-" * 15)
            
    for pokemon in player.pokemons:
        print(pokemon)

    return_screen()