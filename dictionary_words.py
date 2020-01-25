f = open('words.txt', 'r')

words = f.readlines()
for line in words:
    num = 0
    print("Word:" + line)
    num += 1

f.close()
