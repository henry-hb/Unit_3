"""
Henry Hall-Brown

10-4. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
10-5. Guest Book: Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file. Quit when
user types "q"
"""

from pathlib import Path

path1 = Path("Unit3_HW2/guest.txt")
name = input("What is your name? ")
path1.write_text(name)

path2 = Path("Unit3_HW2/guest_book.txt")
path2.write_text("Guest list:")
name = input("What is your name? ")
while(name.lower() != "q"):
    contents = path2.read_text()
    contents += "\n" + name
    path2.write_text(contents)
    name = input("What is your name? ")
