import random
prefix = open("prefix.txt","r+")
suffix = open("suffix.txt","r+")
prefix = random.choice(prefix.read().replace("\n","").split(","))
suffix = random.choice(suffix.read().replace("\n","").split(","))
print(prefix+suffix+str(random.randrange(10000)).zfill(4))
