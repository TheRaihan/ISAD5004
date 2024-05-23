# Python production code for ISE worksheet 8.

def printCoordinates(x, y, z):
    print("({:.2f},{:.2f},{:.2f})".format(x, y, z))


def readChar(validChars):
    line = input()
    while len(line) != 1 or validChars.find(line) == -1:
        line = input()
    return line[0]


def guessingGame(number):
    guess = int(input("Enter an integer: "))
    
    while guess != number:
        if guess > number:
            print("Too high.")
        
        else:
            print("Too low.")
    
        guess = int(input("Enter an integer: "))
        
    print("Correct!")


def sumFile(filename):
    sum = 0.0
    try:
        with open(filename) as inFile:         # Raises OSError
            content = inFile.read().split()
            for word in content:
                sum += float(word)
            
    except OSError:
        sum = -1.0
        
    return sum


def saveData(filename, name, health, score):
    success = True
    try: #case 1
        with open(filename, mode = "w") as writer: # Raises OSError
            writer.write("name: " + name + "\n")
            writer.write("health: " + str(health) + "\n")
            writer.write("score: " + str(score) + "\n")
            if health <= 0.0: #3
                writer.write("status: dead\n")
            else:
                if score >= 100: #4
                    writer.write("status: won\n")
                else: #5 
                    writer.write("status: alive\n")
                    
    except OSError: #case 2
        success = False
        
    return success



