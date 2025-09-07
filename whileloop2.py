password = "learn coding"

input_password = input("Enter password: ")

while input_password != password:
    print("Wrong password, try again!")
    input_password = input("Enter password: ")

print("Unlocked!!")