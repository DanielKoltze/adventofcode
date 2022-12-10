file = open("10/10.txt", "r")
lines = file.readlines()
cycles = [20,60,100,140,180,220,2000]
cyclesAnswer = []
def solve():
    cycleNumber = 0
    cycle = 0
    result = 1
    for line in lines:
        line = line.strip().split(" ")
        if(line[0] == "noop"):
            cycle += 1
            if(cycle == cycles[cycleNumber]):
                    placeholder = result
                    cyclesAnswer.append(placeholder * cycles[cycleNumber])
                    cycleNumber += 1
        else:
            for i in range(2):
                cycle += 1
                if(cycle == cycles[cycleNumber]):
                    placeholder = result
                    cyclesAnswer.append(placeholder * cycles[cycleNumber])
                    cycleNumber += 1
                if(i == 1):
                    result += int(line[1])
    answer = 0
    for number in cyclesAnswer:
        answer += number
    print(answer)
        

solve()