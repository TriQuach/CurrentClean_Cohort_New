from source.CurrentClean_Clustering import *
from itertools import combinations

class PairAppearance:
    def __init__(self, nameWindow, isAppeared, key, nameCohort):
        self.nameWindow = nameWindow
        self.isAppeared = isAppeared
        self.key = key
        self.nameCohort = nameCohort

def makeCombination(array):
    res = []
    for i in range(2, len(array) + 1):
        comb = combinations(array, i)
        for i in list(comb):
            concat = '-'.join(i)
            res.append(concat)

    return res

def getArrayCombination(dict, window):
    rightDict = dict[window]
    arrayAllCombination = []
    for cohort in rightDict:
        arrayEntities = rightDict[cohort]
        combination = makeCombination(arrayEntities)
        arrayAllCombination.extend(combination)
    return arrayAllCombination

def countAppearance(dict, array):
    for i in array:
        if (i in dict):
            count = dict[i]
            count += 1
            dict[i] = count
        else:
            dict[i] = 1


def groupEntitiesApearance(dict):
    hashMapAppearance = {}
    for window in dict:
        rightDict = dict[window]
        arrayAllCombination = getArrayCombination(dict,window)
        countAppearance(hashMapAppearance,arrayAllCombination)
    return hashMapAppearance


threshold1 = 3.0
threshold2 = 5.0
threshold3 = 12.0

threshold4 = 13.0
threshold5 = 19.0

threshold6 = 19.5
threshold7 = 20.0

threshold8 = 21.0
resDict = CurreanClean_Clustering_1stRound(threshold1, threshold2,threshold3, threshold4,threshold5,threshold6,threshold7,threshold8)
hashMapAppearance = groupEntitiesApearance(resDict)
sorted_hashMapAppearance = sorted(hashMapAppearance.items(), key=lambda kv: kv[1], reverse=True)
print(dict(sorted_hashMapAppearance))

