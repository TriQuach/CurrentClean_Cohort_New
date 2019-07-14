import pandas as pd
import datetime

listID = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80']


def readFile(fileName):
    f = open(fileName, "r")
    f2 = open("/Users/triquach/Documents/CurrentClean_CohortNew/data/mimic_20.txt", "w+")
    for line in f:
        word = line.split(',')
        ID = word[1]
        if (ID in listID):
            f2.write(line)
    f2.close()

readFile("/Users/triquach/Documents/CurrentClean_CohortNew/data/mimic_half.txt")
# #
# b = []
# for i in range(1,91):
#     b.append(str(i))
# print(b)



