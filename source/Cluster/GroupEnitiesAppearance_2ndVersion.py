from source.Cluster.RemoveOverlap_2ndVersion import *
from source.Cluster.CurrentClean_Clustering import *
from itertools import combinations

class PairAppearance:
    def __init__(self, nameWindow, count):
        self.nameWindow = nameWindow
        self.count = count

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

def countAppearance(dict, array, window):
    for i in array:
        if (i in dict):
            rightDict = dict[i]
            rightDict['count'] += 1
            windows = rightDict['windows']
            windows.append(window)
            rightDict['windows'] = windows
            dict[i] = rightDict

        else:
            rightDict = {}
            rightDict['count'] = 1
            temp = []
            temp.append(window)
            rightDict['windows'] = temp
            dict[i] = rightDict



def groupEntitiesApearance(dict):
    hashMapAppearance = {}
    for window in dict:
        rightDict = dict[window]
        arrayAllCombination = getArrayCombination(dict,window)
        countAppearance(hashMapAppearance,arrayAllCombination, window)
    return hashMapAppearance



threshold1 = 3.0 #1

threshold2 = 5.0 #2
threshold3 = 12.0 #2

threshold4 = 13.0 #3
threshold5 = 19.0 #3

threshold6 = 19.5 #4
threshold7 = 20.0 #3

threshold8 = 21.0 #5


print('---------*********---------')
print('lower threshold = ' + str(threshold1))
print('middle threshold = [' + str(threshold2) + "," + str(threshold3) + ']')

print('upper threshold = ' + str(threshold4))

print("CurrentClean-Cohort algorithm is running...")

print('---------*********---------')

resDict = removeOverlap_2ndVersion(resDict, dictKL_AllEntities)
# resDict = CurreanClean_Clustering_1stRound(threshold1, threshold2,threshold3, threshold4,threshold5,threshold6,threshold7,threshold8)

# print(resDict)
#
hashMapAppearance = groupEntitiesApearance(resDict)
sorted_hashMapAppearance = sorted(hashMapAppearance.items(), key=lambda kv: kv[1]['count'], reverse=True)
print(sorted_hashMapAppearance)

