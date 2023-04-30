print("this application will add every number you tell it together, after you enter y")
command = []
while (inputTXT := input()) != "y":
    command.append(int(inputTXT))
out = 0
for i in range(len(command)):
    out += command[i]
print(out)