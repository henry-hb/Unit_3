from pathlib import Path

path = Path("lesson2/programming.txt")
path.write_text("I love Python!!\nJava is pretty good too")
contents = path.read_text()
contents += "\nI love to code"
path.write_text(contents)