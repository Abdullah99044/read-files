import time

 

with open('zentext.txt' , 'r' ) as f:
    zen_lines = f.readline()
    while zen_lines:
        time.sleep(1)
        zen_lines = f.readline()
        print(zen_lines )


 