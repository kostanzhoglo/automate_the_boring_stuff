import sys

def collatz(number):
    if number % 2 == 0:
        answer = number // 2
    else:
        answer = number * 3 + 1

    while answer == 1:
        print(answer)
        sys.exit()

    while answer != 1:
        print(answer)
        number = answer
        return collatz(number)

real_integer = False
while not real_integer:
    number_string = input("Please enter a whole number: ")
    try: 
        number = int(number_string)
        # if int(number) worked, then user has entered a real integer and we can move on.
        real_integer = True
    except ValueError:
        print("Only whole integers are accepted.  I bet you didn't enter a whole integer.")
collatz(number)




# def collatz(number):

#     if number % 2 == 0:
#         print(number // 2)
#         return number // 2

#     elif number % 2 == 1:
#         result = 3 * number + 1
#         print(result)
#         return result

# n = input("Give me a number: ")
# while n != 1:
#     n = collatz(int(n))
