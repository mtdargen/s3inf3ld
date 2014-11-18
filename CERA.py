# Comedy Expelling Robot Apparatus
# by Matt Dargen

import random

print("\n\tC.E.R.A.")
print("COMEDY EXPELLING ROBOT APPARATUS\n")

r = random.Random()
fnames = ["jerry.txt","louis.txt"]
n = choice = -1

print("CHOOSE")
print("1. Jerry Seinfeld")
print("2. Louis CK")
choice = int(input(">>> "))
while choice < 1 or choice > 2:
    print("\tno")
    choice = int(input(">>> "))

print("HOW MANY GRAMS? [2-4]")
n = int(input("N = "))
while n < 2 or n > 4:
    print("\tno")
    n = int(input("N = "))

f = open(fnames[choice-1],'r')

grams = f.read().lower().split()

if n == 2:
    grams = zip(grams, grams[1:])
elif n == 3:
    grams = zip(grams,grams[1:],grams[2:])
elif n == 4:
    grams = zip(grams, grams[1:], grams[2:], grams[3:])

while True:
        g = r.choice([x for x in grams if x[0] == "<start>"])
        joke = ""
        while g[n-1] != "<end>":

                if n == 2: g = r.choice([x for x in grams if (x[0] == g[1])])
                elif n == 3: g = r.choice([x for x in grams if (x[0] == g[1]) and (x[1] == g[2])])
                elif n == 4: g = r.choice([x for x in grams if (x[0] == g[1]) and (x[1] == g[2]) and (x[2] == g[3])])

                if g[0] == "<start>":
                    joke += "\n"
                elif g[0] == "<end>":
                    break
                else:
                    joke += g[0] + " "

        if n == 3: joke += g[1]
        elif n == 4: joke += g[1] + " " + g[2]

        print(joke)
        raw_input("\n ... \n")
f.close()
