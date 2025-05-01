from pathlib import Path
import json

song_info = {}
song_info["Artist"] = "David Bowie"
song_info["Title"] = "Heroes"
song_info["Release Year"] = 1977
song_info["Modern"] = False

print(song_info)

path = Path("lesson3/song_info.json")
contents = json.dumps(song_info) #convert python dictionary to json format
path.write_text(contents)
"""
contents = path.read_text()
song_info = json.loads(contents) #converts json to python dictionary
"""