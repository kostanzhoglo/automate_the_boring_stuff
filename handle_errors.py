def division(divideBy):
    try:
        return 42 / divideBy
    except:
        print("Dude, you can't divide by 0 man.")

print(division(2))
print(division(12))
print(division(0))
print(division(3))


def divider(divideBy):
    return 42 / divideBy

try:
    print(divider(2))
except:
    print("Seriously, still can't divide by 0.")
     
try:
    print(divider(12))
except:
    print("Seriously, still can't divide by 0.") 

try:
    print(divider(0))
except:
    print("Seriously, still can't divide by 0.")

try: 
    print(divider(3))
except:
    print("Seriously, still can't divide by 0.")  
