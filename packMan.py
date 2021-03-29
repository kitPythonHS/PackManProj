
import random

print("Pack Man Game Started.\n")
print("[WARNING] Ghost Come...\n")

print("[1. Run] [2. Use Item] [3. Fight]")
choose = int(input("INPUT >> "))

randomVar = random.randint(0, 100)
print("Check Rand Var >> ", randomVar)

if choose == 1:
    randomVar /= 10
    if randomVar < 2:
        print("Character RUN")
    else:
        print("Character DEAD.....")
elif choose == 2:
    print("Charater Using the ITEM")
elif choose == 3:
    print("Character Dead")