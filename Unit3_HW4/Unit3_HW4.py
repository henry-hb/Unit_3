from pathlib import Path
import json

path = Path("Unit3_HW4/favorite_number.json")
num = path.read_text()
if(num.isdigit()):
    print(path.read_text())
else:
    number = input("What is your favorite number? ")

    contents = json.dumps(number) #converts to json format
    path.write_text(contents) #writes to username.json

    fav_number = json.loads(contents)
    print(f"I know your favorite number! It's {fav_number}")



path2 = Path("Unit3_HW4/remember_me.json")
info = {}
info["name"] = input("What is your name? ")
info["age"] = input("What is your age? ")
contents2 = json.dumps(info)
path2.write_text(contents2)
string = json.loads(contents2)
print(string)