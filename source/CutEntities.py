import pandas as pd
import datetime

listID = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']

def readFile(fileName):
    f = open(fileName, "r")
    f2 = open("../data/mimic_20.txt", "w+")
    for line in f:
        word = line.split(',')
        ID = word[1]
        if (ID in listID):
            f2.write(line)
    f2.close()

readFile("../data/mimic_half.txt")

# b = []
# for i in range(1,46):
#     b.append(str(i))
# print(b)



