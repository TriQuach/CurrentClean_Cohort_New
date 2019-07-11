from source.Cluster.CurrentClean_Clustering_2ndVersion import *

class KLScoreOnGroup:
    def __init__(self, group, KLScore):
        self.group = group
        self.KLScore = KLScore

def getAllGroupsOfOneWindow(rightDict):
    arr = []
    for key in rightDict:
        temp = []
        temp.append(key)
        temp.extend(rightDict[key]['cluster'])
        temp.sort(key=float)
        arr.append(temp)
    return arr


def removeDuplicateGroup(arr):
    b_set = set(tuple(x) for x in arr)
    k = [list(x) for x in b_set]
    return k


def findAllGroupContainMainID(mainID, removeDuplicate):
    arr = []
    for group in removeDuplicate:
        if (mainID in group):
            arr.append(group)
    return arr


def KLScoreForEachGroup(containers, mainID, dictKL_AllEntities,window):
    currentWin = window.split('_')[1]
    arrObj = []
    for group in containers:
        arrKL = []
        for element in group:
            if (element != mainID):
                arrKL.append(dictKL_AllEntities[mainID][element][int(currentWin)])
        if (len(arrKL) != 0):
            obj = KLScoreOnGroup(group,np.mean(arrKL))
        else:
            obj = KLScoreOnGroup(group, 0.0)
        arrObj.append(obj)

    arrObj.sort(key=lambda x: x.KLScore)
    return arrObj[0], arrObj[1:len(arrObj)]

def removeIDInOtherGroups(keep, needToRemove, removedDuplicateArray):

    for obj in needToRemove:
        for group in removedDuplicateArray:
            if (obj.group == group):
                for elements in list(group):
                    if (elements in keep.group):
                        group.remove(elements)


def mergeChildrenGroup(removeDuplicate):
    temp = removeDuplicate.copy()
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if (all(elem in temp[i] for elem in temp[j])):
                if (temp[j] in removeDuplicate):
                    removeDuplicate.remove(temp[j])
            elif(all(elem in temp[j] for elem in temp[i])):
                if (temp[i] in removeDuplicate):
                    removeDuplicate.remove(temp[i])

def removeOverlap_2ndVersion(resDict, dictKL_AllEntities):
    removeDict = {}
    for window in resDict:
        rightDict = resDict[window]
        allGroupOneWin = getAllGroupsOfOneWindow(rightDict)
        removeDuplicate = removeDuplicateGroup(allGroupOneWin)
        for mainID in rightDict:
            containers = findAllGroupContainMainID(mainID, removeDuplicate)
            keep, remove = KLScoreForEachGroup(containers, mainID, dictKL_AllEntities, window)
            removeIDInOtherGroups(keep,remove, removeDuplicate)
            removeDuplicate = removeDuplicateGroup(removeDuplicate)
            # mergeChildrenGroup(removeDuplicate)

            print('zxc')

        

        removeDict[window] = removeDuplicate

    return removeDict




dictKL_AllEntities, resDict = CurreanClean_Clustering()



print('---------*********---------')

print('threshold clustering = ' + str(constant.THRESHOLD_ENTITIES))

print("CurrentClean-Cohort algorithm is running...")

print('---------*********---------')

removeDict = removeOverlap_2ndVersion(resDict, dictKL_AllEntities)

print('zxc')