#!/bin/usr/python3
# Task: Switches between 2 radio streams based on external '.counter.dat' file; complex version

import os.path  # check if .counter exists
import subprocess # launch epiphany based on $num

URL1 = www.google.com
URL2 = www.adobe.com

# confirms FILE isn't empty
def check_counter():
    inFile = open('.counter.dat','r')
    line = inFile.readline()
    line = line.strip()
    inFile.close()
    if line == '':
        return False
    else:
        return True

def main():
    if os.path.isfile('.counter.dat') == False or check_counter() == False:
        outFile = open('.counter.dat','w')
        outFile.write('0'+'\n')
        outFile.close()
        main()

    else:
        inFile = open('.counter.dat','r')
        num  = inFile.readline()
        num = int(num)
        inFile.close()

    #increment $num & WRITE to .counter FILE
        outFile = open('.counter.dat','w')
        num += 1
        # convert $num to STRING for persistance
        num = str(num)
        outFile.write(num+'\n')
        outFile.close()

        # convert $num back to INT for division
        num = int(num)

        if num % 2 == 0:  # if $num is EVEN
            subprocess.Popen(['epiphany-browser',URL1])  # open URL1, real-world should be a 'STRING'
        else:
            subprocess.Popen(['epiphany-browser',URL2])  # open URL2, real-world should be a 'STRING'

main()
