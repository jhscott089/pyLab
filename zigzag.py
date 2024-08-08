import time, sys
indent = 0 # how many spaces to indent.
indentIncreasing = True # Whether the indent is increasing or not.

try:
        while True: # the main program loop
            print(' ' * indent, end='')
            print('********')
            time.sleep(0.01) # Pause for 1/10 of a second

            if indentIncreasing:
                # Increase the number of spaces:
                indent = indent + 1
                indent = indent + 1
                if indent == 100:
                        # Change diretion
                    indentIncreasing = False
            else:
                    # Decrease the number of spaces:
                    indent = indent - 1
                    if indent == 0:
                        # Chagne direction:
                        indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()