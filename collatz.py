# this is the best version so far. adds validation of all kinds.
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

valid = False   # ensures we keep asking for good input until we get it.

while not valid: 
    num = input("Please enter a positive integer: ")
    try:
        num = int(num)  # make sure input is a number
        if num < 1:     # make sure number is positive
            print("Entering 0 or a negative number is not cool dude.")
        elif num == 1:  # 1 is a special case
            for i in range(1, 4):
                num = collatz(num)
            valid = True
        else:
            while num != 1:
                num = collatz(num)   
            valid = True
    except ValueError:
        print("Aw, cmon, enter a Whole Integer!")


# this was my first attempt. not bad, but i refactored above
# import sys

# def collatz(number):
#     if number % 2 == 0:
#         answer = number // 2
#     else:
#         answer = number * 3 + 1

#     while answer == 1:
#         print(answer)
#         sys.exit()

#     while answer != 1:
#         print(answer)
#         number = answer
#         return collatz(number)

# real_integer = False
# while not real_integer:
#     number_string = input("Please enter a whole number: ")
#     try: 
#         number = int(number_string)
#         # if int(number) worked, then user has entered a real integer and we can move on.
#         real_integer = True     # this will take us out of the while loop
#     except ValueError:
#         print("Only whole integers are accepted.  I bet you didn't enter a whole integer.")
# collatz(number)




# This is a clean solution, but doesn't protect against 0 or negative numbers
#  def collatz(number):

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
