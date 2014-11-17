# Comedy Expelling Robot Apparatus
# by Matt Dargen

import random

print("s3inf3ld\n")

r = random.Random()
jerry = open("jerry.txt",'r')


trigrams = jerry.read().lower().split()
trigrams = zip(trigrams,trigrams[1:],trigrams[2:])

while True:
    tg = r.choice([x for x in trigrams if x[0] == "<start>"])
    joke = ""
    while tg[2] != "<end>":
            tg = r.choice([x for x in trigrams if (x[0] == tg[1]) and (x[1] == tg[2])])
            if tg[0] == "<start>":
                joke += "\n"
            else:
                joke += tg[0] + " "
    joke += tg[1]
    print(joke)
    raw_input("\n ... \n")

jerry.close()
