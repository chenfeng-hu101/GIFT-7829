import random
try:
    with open("F://PycharmProject//.venv//name_list.txt","r",encoding="utf-8") as file:
        names=file.readlines()
        names=[name.strip() for name in names]
    chosen_name = random.choice(names)
    print(chosen_name)
except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")