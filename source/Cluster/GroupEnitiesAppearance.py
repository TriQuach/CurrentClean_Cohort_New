from source.Cluster.CurrentClean_Clustering import *
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



def checkAppearanceInWindows(pair, arrayWindow, dict):
    splitted = pair.split("-")
    arrayPairAppearance = []
    for window in arrayWindow:
        rightDict = dict[window]
        flag = False
        for cohort in rightDict:
            arrayEntitiesInCohort = rightDict[cohort]
            if (all(elem in arrayEntitiesInCohort for elem in splitted) == True):  # 1-39 appears in a given cohort
                pairAppearance = PairAppearance(window, True, pair, cohort)
                arrayPairAppearance.append(pairAppearance)
                flag = True
        if (flag == False):
            pairAppearance = PairAppearance(window,False,pair,'')
            arrayPairAppearance.append(pairAppearance)
    return arrayPairAppearance

def isInCheckArray(setKeyCheck, key):
    splitted = key.split('-')
    for i in range(1, len(splitted)):
        temp = splitted[0:i]
        join = '-'.join(temp)
        if (join in setKeyCheck):
            return True

    return False



def countAppearance(arrayPairAppearance):
    count = 0
    for i in arrayPairAppearance:
        if (i.isAppeared == True):
            count += 1
    return count

def groupEntitiesApearance(dict):
    arrayWindow = []
    dictPairAppearance = {}
    setKeyCheck = set()
    index = 0
    for key in dict:
        arrayWindow.append(key)
    for window in dict:
        arrayAllCombination = getArrayCombination(dict,window)
        for element in arrayAllCombination:
            if (isInCheckArray(setKeyCheck,element) == False):
                arrayWindowRemain = arrayWindow[index + 1 : len(arrayWindow) + 1]

                arrayPairAppearance = checkAppearanceInWindows(element,arrayWindowRemain,dict)
                dictPairAppearance[element] = arrayPairAppearance
                if (countAppearance(arrayPairAppearance) < constant.THRESHOLD_APPEARANCE):
                    setKeyCheck.add(element)

    return dictPairAppearance


# threshold1 = 2.0
# threshold2 = 8.0
# threshold3 = 9.0
# threshold4 = 15.0

threshold1 = 0.1
threshold2 = 0.15
threshold3 = 0.2
threshold4 = 0.22
resDict = CurreanClean_Clustering_1stRound(threshold1, threshold2,threshold3, threshold4)
dictPairAppearance = groupEntitiesApearance(resDict)
print(dictPairAppearance)