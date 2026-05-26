def calPoints(operations):
    scores = []
    for i in range(len(operations)):
        if len(scores) > 1:
            if operations[i] == "C":
                scores.pop(-1)
            elif operations[i] == "D":
                scores.append(int(scores[-1] * 2))
            elif operations[i] == "+":
                scores.append(int(scores[-1] + scores[-2]))
            else:
                scores.append(int(operations[i]))
        else:
            scores.append(int(operations[i]))

    return sum(scores)

print(calPoints(["1","2","+","C","5","D"]))