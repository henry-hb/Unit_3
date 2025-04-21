#10-1
from pathlib import Path
path = Path("Unit3_HW1/learning_python.txt")
contents = path.read_text()
print(contents)
lines = contents.splitlines()
for i in lines:
    print(i)
#10-2
print("")
new_message = contents.replace("Python","C")
print(new_message)