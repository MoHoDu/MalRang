def printTo100(num):
    print(num)
    if num == 100:
        quit()
    printTo100(num + 1)

printTo100(1)