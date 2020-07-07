import time, sys
indent = 0                  # how many spaces to indent
indentIncreasing = True     # is Indentation increasing or no?

try:
    while True:             # main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.05)     # pause for 1/10 sec

        if indentIncreasing:
            # increase number of spaces beginning of line
            indent += 1
            if indent == 20:    # change direction
                indentIncreasing = False
        
        else:
            # decrease number of spaces beginning of line
            indent -= 1
            if indent == 0:     # change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
