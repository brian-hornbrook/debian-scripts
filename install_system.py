import os

for file in os.listdir("system"):
    os.system(f"sudo bash ./system/{file}")
    print(file)