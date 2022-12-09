file = open("6december.txt","r")
line = file.read()

def calc(number):
    result = number
    for char in range(len(line)-number):
        string = line[char:char+number]
        if allEqual(string):
            result += 1
        else:
            return result 

def allEqual(string):
    for char in range(len(string)):
        for next in range(char+1,len(string)):
            if string[char] == string[next]:
                return True
    return False
print(calc(14))