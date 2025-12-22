import os

choice = input("Do you want to shutdown? (yes/no): ")

if choice.lower() == "yes":
    os.system("shutdown /s /t 5")
else:
    print("Shutdown cancelled")
