def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

real_number = False
while not real_number:
    num = input("Input a positive integer: ")
    try:
        num = int(num)
        if num < 1:
            print("Hey enter a POSITIVE integer please!")
        elif num == 1:
            for i in range(3):
                num = collatz(num)
            real_number = True
        else:
            while num != 1:
                num = collatz(num)
            real_number = True
    except ValueError:
        print("C'mon, enter an INTEGER dude")