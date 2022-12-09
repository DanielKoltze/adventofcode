file = open("2december.txt","r")
lines = file.readlines()

def calc():
    result = 0
    for line in lines:
        line = line.strip()
        split = line.split(" ")
        opponent = split[0]
        output = split[1]
        answer = calcHand(opponent,output)
        if answer == "A X":
            result += 4
        elif answer == "A Y":
            result += 8
        elif answer == "A Z":
            result += 3
        elif answer == "B X":
            result += 1
        elif answer == "B Y":
            result += 5
        elif answer == "B Z":
            result += 9
        elif answer == "C X":
            result += 7
        elif answer == "C Y":
            result += 2
        elif answer == "C Z":
            result += 6
    print(result)

def calcHand(opponent,output):
    #win
    answer = ""
    if(opponent == "A" and output == "X"):
        answer = "A Z"
    elif(opponent == "A" and output == "Y"):
        answer = "A X"
    elif(opponent == "A" and output == "Z"):
        answer = "A Y"
    elif(opponent == "B" and output == "X"):
        answer = "B X"
    elif(opponent == "B" and output == "Y"):
        answer = "B Y"
    elif(opponent == "B" and output == "Z"):
        answer = "B Z"
    elif(opponent == "C" and output == "X"):
        answer = "C Y"
    elif(opponent == "C" and output == "Y"):
        answer = "C Z"
    elif(opponent == "C" and output == "Z"):
        answer = "C X"
    return answer




calc()