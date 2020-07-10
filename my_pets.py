myPets = ["franny", "zooey", "seymour", "carpenter"]
name = input("Enter a pet name: ")
if name not in myPets:
    print("I don't have a pet named " + name + ".")
else:
    print(name + " is my pet yesiree!")