from pathlib import Path
import json
import requests
import urllib.request

POKE_URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = urllib.request.urlopen(POKE_URL,timeout=10) #get response from URL

pokemon = json.load(response) #converts API json response to a python dictionary
print(pokemon["forms"][0]["url"])
print(pokemon["types"][0]["type"]["name"])
print(pokemon["abilities"][0]["ability"]["name"])
print(pokemon["abilities"][1]["ability"]["name"])

for ability in pokemon["abilities"]:
    print(f"Name: {ability['ability']['name']}")

print("")
for moves in pokemon["moves"]:
    print("Name: " + moves["move"]["name"])