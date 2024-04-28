#!/usr/bin/env python3

import os
from time import sleep

try:
    from colorama import init, Fore
except ImportError:
    print("\ncolorama not installed".title())
    exit(1)

init()
red = Fore.RED
ylw = Fore.YELLOW
grn = Fore.GREEN
blu = Fore.BLUE
rst = Fore.RESET

def Addition(a, b):
    return a + b

def Substruction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def Division(a, b):
    return a / b

while True:
    try:
        print(grn, """
         --  --  --  --  --  --  --  --  --  --  --
        ; [*] Please choose one of the following:  ;
        ;                                          ;
        ;   [1]. Addition                          ;
        ;   [2]. Substruction                      ;
        ;   [3]. Multiplication                    ;
        ;   [4]. Division                          ;
         --  --  --  --  --  --  --  --  --  --  -- \n""", rst)

        read = input(ylw + "\nSelect Number: " + rst)
    
        def main():
            if read == "1":
                read1 = float(input(blu + "\n[*] Type the number: " + rst))
                read2 = float(input(blu + "[*] Type the number: " + rst))
                result1 = Addition(read1, read2)
                res1 = print(grn, f"\nResult: {ylw}{read1}{rst} + {ylw}{read2}{rst} = {red}{result1}{rst}\n")
                with open('result.txt', 'w') as file:
                    file.write(res1)
                    sleep(5)
                    os.system("clear")
                    return

            elif read == "2":
                read1 = float(input(blu + "\n[*] Type the number: " + rst))
                read2 = float(input(blu + "[*] Type the number: " + rst))
                result2 = Substruction(read1, read2)
                print(grn, f"\nResult: {ylw}{read1}{rst} + {ylw}{read2}{rst} = {red}{result2}{rst}\n")
                sleep(5)
                os.system("clear")            
                return

            elif read == "3":
                read1 = float(input(blu + "\n[*] Type the number: " + rst))
                read2 = float(input(blu + "[*] Type the number: " + rst))
                result3 = Multiplication(read1, read2)
                print(grn, f"\nResult: {ylw}{read1}{rst} + {ylw}{read2}{rst} = {red}{result3}{rst}\n")
                sleep(5)
                os.system("clear")
                return

            elif read == "4":
                read1 = float(input(blu + "\n[*] Type the number: " + rst))
                read2 = float(input(blu + "[*] Type the number: " + rst))
                result4 = Division(read1, read2)
                print(grn, f"\nResult: {ylw}{read1}{rst} + {ylw}{read2}{rst} = {red}{result4}{rst}\n")
                sleep(5)
                os.system("clear")
                return

            else:
                print(red, "\n[!] Invalid Input. Please type correctly", rst)
                sleep(3)
                os.system("clear")
        main()

    except KeyboardInterrupt:
        print(red, "\n\nUser request exitting...\n", rst)
        sleep(1)
        os.system("clear")
        exit()

    except ValueError:
            print(red, "\n[!] Value Error. Please type correctly", rst)
            sleep(3)
            os.system("clear")
            exit()
