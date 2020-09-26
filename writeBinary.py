import random

f = open("binaryFile.txt", "w")
for i in range(0, 10000000):
    f.write(str(random.randint(0, 1)))
f.close()
    
