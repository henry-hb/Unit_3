from pathlib import Path
import json

user_name = input("What is your name? ")

path = Path("lesson3/username.json")
contents = json.dumps(user_name) #converts to json format
path.write_text(contents) #writes to username.json