supplies = ["pens", "paper", "pencils", "binders"]

# for index in range(len(supplies)):
#     print("Index " + str(index) + " in supplies list is: " + supplies[index]) 


# ENUMERATE()
print("Supplies List")
for i, item in enumerate(supplies):
    print("Index " + str(i) + ": " + item)