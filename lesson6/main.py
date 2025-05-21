'''
start a virtual enviroment
pip install pillow (*NOT* PIL, I know it's weird)
pip install requests
On windows, tkinter is installed by default
'''

import requests
import io # needed to process the bytes that we will download the sprite in
from pathlib import Path # if you want to create a cache of sprites
import tkinter as tk
from PIL import Image, ImageTk # allows us to manipulate images
import random


# ---------- constants ----------
POKE_COUNT = 1025                              # adjust if new pokemon come out (is this a thing?)
API_URL    = "https://pokeapi.co/api/v2/pokemon/{}" # we will use {} later for substitution with .format()

# ---------- GUI Stuff ----------
root = tk.Tk()
root.title("Random Pokémon Generator")
root.geometry("300x500")
root.resizable(False, False)
        
def fetch_pokemon(pokemon_id: int) -> dict:
    request = requests.get(API_URL.format(pokemon_id),timeout=10)
    request.raise_for_status()
    data = request.json()
    formatted_data = {
        "id":           pokemon_id,
        "name":         data["name"].title(),
        "types":        [t["type"]["name"] for t in data["types"]], 
        "weight_kg":    data["weight"]/10,
        "sprite":       data["sprites"]["front_default"]
    }
    return formatted_data

#pokemon_id is not needed
def fetch_image(url: str) -> ImageTk.PhotoImage:
    #url is the url of the sprite of the pokemon
    img_bytes = requests.get(url,timeout=10).content
    pillow_image = Image.open(io.BytesIO(img_bytes)).resize((200,200))
    tk_image = ImageTk.PhotoImage(pillow_image)
    return tk_image

def show_pokemon(pokemon_id:int)->None:
    try:
        pokemon_data = fetch_pokemon(pokemon_id)
        #url of the sprite passed as argument to get image of pokemon
        tk_image = fetch_image(pokemon_data["sprite"])

        root.img_label.photo = tk_image
        root.img_label.config(image=tk_image)

        types = " / ".join(pokemon_data["types"]).title() # convert dict to string
        root.info_label.config(
            text=f"{pokemon_data['name']}  (#{pokemon_data['id']})\n"
                    f"Type: {types}\n"
                    f"Weight: {pokemon_data['weight_kg']} kg"
        )
    except Exception as e:
        root.info_label.config(text=f"Error: {e}")

# widgets
root.img_label = tk.Label()
root.img_label.pack(pady=(10, 5))
root.info_label = tk.Label(font=("Helvetica", 12), justify="center")
root.info_label.pack(pady=(0, 10))

root.btn = tk.Button(
    text="Show Pokémon",
    font=("Helvetica", 14, "bold"),
    #lambda makes it so you can pass arguments to command without the parentheses making it run automatically
    command = lambda : show_pokemon(random.randint(0,POKE_COUNT))
)
root.btn.pack(fill="x", padx=20, pady=5)

root.mainloop()