# © 2026 Qwentext Studios™. All rights reserved.
# Created by Ethan Zofchak
# Unauthorized actions including but not limited to: 
# replication, modification, distribution, reverse engineering, or decompilation of this file, via any medium is strictly prohibited.
# For licensing information or distribution inquiries, please contact: support@qwentextstudios.com
# Version 1.0.0

import time

class C:
    RED = '\033[91m'
    GRN = '\033[92m'
    YEL = '\033[93m'
    G_YEL = '\033[38;5;178m'
    BLU = '\033[94m'
    MGNT = '\033[95m'
    CYN = '\033[96m'
    END = '\033[0m' 
    BLD = '\033[1m'
    ULI = '\033[4m'
    ITA = '\033[3m'     
    DBLU = '\033[38;5;18m' 
    DBT = '\033[38;5;20m'

# Logic functions with try/except to prevent crashes on non-integer input
def sumadd():
    try:
        time.sleep(0.4)
        print("Enter the first number.")
        num1 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Enter the second number.")
        num2 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Calculating...")
        time.sleep(0.4)
        print(f"{C.RED}SUM = {C.END}{num1 + num2}\n")
    except ValueError:
        print(f"{C.RED}Error: Please enter numbers only.{C.END}\n")

def subadd():
    try:
        time.sleep(0.4)
        print("Enter the first number.")
        num3 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Enter the second number.")
        num4 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Calculating...")
        time.sleep(0.4)
        print(f"{C.RED}DIF = {C.END}{num3 - num4}\n")
    except ValueError:
        print(f"{C.RED}Error: Please enter numbers only.{C.END}\n")

def muladd():
    try:
        time.sleep(0.4)
        print("Enter the first number.")
        num5 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Enter the second number.")
        num6 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Calculating...")
        time.sleep(0.4)
        print(f"{C.RED}PRO = {C.END}{num5 * num6}\n")
    except ValueError:
        print(f"{C.RED}Error: Please enter numbers only.{C.END}\n")

def quoadd():
    try:
        time.sleep(0.4)
        print("Enter the first number.")
        num8 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Enter the second number.")
        num9 = int(input(f"{C.DBLU}>>{C.END}"))
        time.sleep(0.4)
        print("Calculating...")
        time.sleep(0.4)
        if num9 == 0:
            print(f"{C.RED}Error: Cannot divide by zero.{C.END}\n")
        else:
            print(f"{C.RED}QUO = {C.END}{num8 / num9}\n")
    except ValueError:
        print(f"{C.RED}Error: Please enter numbers only.{C.END}\n")

# Main Application Loop
while True:
    print(f"\n{C.G_YEL}Qwentext Studios™, Est. 2025{C.END}")
    print(f"{C.G_YEL}© 2026 Qwentext Studios™. All rights reserved.{C.END}")
    print(f"\n{C.BLD}1 to calculate, 2 to quit.{C.END}")
    
    qaz = input("> ")
    
    if qaz == "1":
        print("\nPlease enter a number 1 - 4 for each operation.")
        print("1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division")

        optype = input('>')
        if optype == "1":
            sumadd()
        elif optype == "2":
            subadd()
        elif optype == "3":
            muladd()
        elif optype == "4":
            quoadd()
        else:
            print(f"{C.RED}Invalid input, try again.{C.END}")

    elif qaz == "2":
        print("Exiting...")
        break
    else:
        print(f"{C.RED}Invalid input, try again.{C.END}")