import os

for file in os.listdir("apps"):
    os.system(f"sudo bash ./apps/{file}")
    print(file)