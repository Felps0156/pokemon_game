from api.pokeapi import get_random_pokemon
from screen import clean_screen, return_screen


def open_random_pokemon(player):
    clean_screen()
    if player.pokecoin >= 1:
        player.pokecoin -= 1
        
        pokemon, rarity = get_random_pokemon()
        player.pokemons.append(pokemon.name)

        print(f"Você sorteou {pokemon.name}")
        print(f"Raridade: {rarity}")

        print(f"Quantidade de moedas: {player.pokecoin}")
        
        return_screen()
    else:
        print("Você não possui mais moedas")
        return_screen()