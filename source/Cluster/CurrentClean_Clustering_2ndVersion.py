from source.Similarity.KL_OneAttr_MultipleEntities import *
import numpy as np
class ClusterOnMainID:
    def __init__(self, clusterName, KLScore):
        self.clusterName = clusterName
        self.KLScore = KLScore

def isInTheSameCluster(key1,key2, cluster1, cluster2):
    if (key1 in cluster1 and key2 in cluster1):
        return True
    if (key1 in cluster2 and key2 in cluster2):
        return True
    return False

def CurreanClean_Clustering(threshold):
    listAttr = ['HR']
    dictEntitiesVal = normalizeDictArray(listAttr)
    listID = getAllEntitiesID(dictEntitiesVal)
    # listID = ['1','2','83','39']
    dictKL_AllEntities = getKLallEntities(dictEntitiesVal, listID, 'HR')

    cluster1 = [] # cluster that has values that are less than threshold
    cluster2 = []




    for key in dictKL_AllEntities:
        dictRight = dictKL_AllEntities[key]
        for key2 in dictRight:
            KLScore_1stWindow = dictRight[key2][0]
            if (KLScore_1stWindow < threshold):
                if (key not in cluster1):
                    if (isInTheSameCluster(key,key2,cluster1,cluster2) == False):
                        cluster1.append(key)
                        if (key in cluster2):
                            cluster2.remove(key)
                if (key2 not in cluster1):
                    if (isInTheSameCluster(key, key2, cluster1, cluster2) == False):
                        cluster1.append(key2)
                        if (key2 in cluster2):
                            cluster2.remove(key2)
                if (key in cluster2):
                    if (isInTheSameCluster(key, key2, cluster1, cluster2) == False):
                        cluster2.remove(key)
                if (key2 in cluster2):
                    if (isInTheSameCluster(key, key2, cluster1, cluster2) == False):
                        cluster2.remove(key2)
            else:
                if (key not in cluster1 and key not in cluster2):
                    cluster1.append(key)
                if (key2 not in cluster1 and key2 not in cluster2):
                    cluster2.append(key2)


    return cluster1,cluster2

def clusterOneWindow(array,threshold1, threshold2,threshold3, threshold4,threshold5,threshold6,threshold7,threshold8):
    cluster1 = []  # cluster that has values that are less than threshold
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []  # cluster that has values that are less than threshold
    cluster6 = []

    for i in range(len(array)):
        if (array[i] < threshold1):
            cluster1.append(str(i+2))
        elif (array[i] > threshold2 and array[i] < threshold3):
            cluster2.append(str(i+2))
        elif (array[i] > threshold4 and array[i] < threshold5):
            cluster3.append(str(i+2))
        elif (array[i] > threshold6 and array[i] < threshold7):
            cluster4.append(str(i+2))
        elif (array[i] > threshold8):
            cluster5.append(str(i + 2))

        else:
            cluster6.append(str(i+2))
    return cluster1, cluster2, cluster3,cluster4,cluster5,cluster6




def CurreanClean_Clustering():
    listAttr = ['HR']
    dictEntitiesVal = normalizeDictArray(listAttr)
    listID = getAllEntitiesID(dictEntitiesVal)
    # listID = ['1','2','83','39']
    dictKL_AllEntities = getKLallEntities(dictEntitiesVal, listID, 'HR')


    resDict = {}

    for mainID in listID:
        rightDict = dictKL_AllEntities[mainID]

        for smallerKey in rightDict:
            arrayKLWindows = rightDict[smallerKey]
            for i in range(len(arrayKLWindows)):
                cluster1 = []
                cluster2 = []
                if (arrayKLWindows[i] < constant.THRESHOLD_ENTITIES):
                    currentWindow = 'window_' + str(i)
                    if (currentWindow in resDict):
                        if (mainID in resDict[currentWindow]):
                            clustersOfMainID = resDict[currentWindow][mainID]
                        else:
                            resDict[currentWindow][mainID] = {}
                            clustersOfMainID = resDict[currentWindow][mainID]
                        if ('cluster' in clustersOfMainID):
                            cluster_1 = clustersOfMainID['cluster']
                            cluster_1.append(smallerKey)
                            resDict[currentWindow][mainID]['cluster'] = cluster_1
                        else:
                            cluster1.append(smallerKey)
                            resDict[currentWindow][mainID]['cluster'] = cluster1


                    else:
                        dictClustersOfMainID = {}
                        cluster1.append(smallerKey)
                        dictClustersOfMainID['cluster'] = cluster1
                        dictMainIDClustersCurrentWindow = {}
                        dictMainIDClustersCurrentWindow[mainID] = dictClustersOfMainID
                        resDict[currentWindow] = dictMainIDClustersCurrentWindow

                # else:
                #     currentWindow = 'window_' + str(i)
                #     if (currentWindow in resDict):
                #         # clustersOfMainID = {}
                #         if (mainID in resDict[currentWindow]):
                #             clustersOfMainID = resDict[currentWindow][mainID]
                #         else:
                #             resDict[currentWindow][mainID] = {}
                #             clustersOfMainID = resDict[currentWindow][mainID]
                #
                #         if ('cluster_2' in clustersOfMainID):
                #             cluster_2 = clustersOfMainID['cluster_2']
                #             cluster_2.append(smallerKey)
                #             resDict[currentWindow][mainID]['cluster_2'] = cluster_2
                #         else:
                #             cluster2.append(smallerKey)
                #             resDict[currentWindow][mainID]['cluster_2'] = cluster2
                #
                #     else:
                #         dictClustersOfMainID = {}
                #         cluster2.append(smallerKey)
                #         dictClustersOfMainID['cluster_2'] = cluster2
                #         dictMainIDClustersCurrentWindow = {}
                #         dictMainIDClustersCurrentWindow[mainID] = dictClustersOfMainID
                #         resDict[currentWindow] = dictMainIDClustersCurrentWindow

    return dictKL_AllEntities, resDict

def getDictClusterName(dict, array, mainID, dictKL_AllEntities, window,clusterName):
    currentWin = window.split('_')[1]
    for entity in array:
        score = dictKL_AllEntities[mainID][entity][int(currentWin)]
        obj = ClusterOnMainID(clusterName,score)
        if (entity in dict[window]):
            arr = dict[window][entity]
            arr.append(obj)
            dict[window][entity] = arr
        else:
            arr = []
            arr.append(obj)
            dict[window][entity] = arr




def getHashMapKLScoreAcrossClusters(dictKL_AllEntities,dict):
    dictRes = {}
    for window in dict:
        dictRes[window] = {}
        rightDict = dict[window]
        for mainID in rightDict:
            cluster_1_2_Dict = rightDict[mainID]
            cluster_1 = cluster_1_2_Dict['cluster']
            # cluster_2 = cluster_1_2_Dict['cluster_2']
            clusterName = 'entity_' + mainID + '_group'
            getDictClusterName(dictRes,cluster_1,mainID,dictKL_AllEntities,window,clusterName)
            # getDictClusterName(dictRes,cluster_2,mainID,dictKL_AllEntities,window,'cluster_2')

    return dictRes

def getSmallesScore(dict):
    for window in dict:
        rightDict = dict[window]
        for entity in rightDict:
            arrayObj = rightDict[entity]
            arrayObj.sort(key=lambda x: x.KLScore)
            temp = arrayObj[0]
            rightDict[entity] = temp
#
def getAllGroupContainer(id,dict):
    res = []
    for key in dict:
        if (key == id):
            tempArr = []
            tempArr.append(key)
            tempArr.extend(dict[key]['cluster'])
            res.append(tempArr)
        else:
            if (id in dict[key]['cluster']):
                tempArr = []
                tempArr.append(key)
                tempArr.extend(dict[key]['cluster'])
                res.append(tempArr)


    return res

def findIntersection(twoDimArray):
    temp = []
    for i in twoDimArray:
        temp.append(set(i))

    return set.intersection(*temp)


def removeOverlap(dict):
    for window in dict:
        rightDict = dict[window]
        for mainID in rightDict:
            allApearance = getAllGroupContainer(mainID, rightDict)
            intersection = findIntersection(allApearance)
            print('n')

# def getAverageKLScore(mainID, dictKL_AllEntities):

#
# def addItselfGroup(dictEntitiyAppearInGroup, dictKL_AllEntities, resDict):
#     for window in dictEntitiyAppearInGroup:
#         rightDict = dictEntitiyAppearInGroup[window]
#         for id in rightDict:
#             array = rightDict[id]
#             averageKLScore

def getAllDictAppearance(mainID, dict):
    resDict = {}
    for id in dict:
        if (mainID in dict[id]['cluster']):
            resDict[id] = dict[id]
    resDict[mainID] = dict[mainID]
    return resDict


def averageKLScore(dictAppear, dictKL_AllEntities, mainID,window):
    currentWin = window.split('_')[1]
    resDict = {}
    for id in dictAppear:
        arr = dictAppear[id]['cluster']
        if (id not in arr):
            arr.append(id)
        arrKLScore = []
        for i in arr:
            if (i != mainID):
                splitted = i.split('_')
                if (len(splitted) == 1):
                    arrKLScore.append((dictKL_AllEntities[mainID][i][int(currentWin)]))
                else:
                    arrKLScore.append((dictKL_AllEntities[mainID][splitted[0]][int(currentWin)]))
        resDict[id] = np.mean(arrKLScore)
    return resDict


def getIDToRemove(dictAverageKLScore):
    sorted_x = sorted(dictAverageKLScore.items(), key=lambda kv: kv[1])
    keep = sorted_x[0]
    remove = sorted_x[1:len(sorted_x)]

    return keep, remove

def deleteOverlaptFromDict(resDict, remove, window, mainID):
    for i in remove:
        cluster = resDict[window][i[0]]['cluster']
        cluster.remove(mainID)
        resDict[window][i[0]]['cluster'] = cluster
        if (i[0] == mainID):
            temp = {}
            temp['cluster'] = cluster
            newName = mainID + '_Removed'
            resDict[window][newName] = temp
            del(resDict[window][mainID])


def newRemoveOverlap(dict, dictKL_AllEntities ):
    for window in dict:
        rightDict = dict[window]
        for mainID in rightDict:
            split = mainID.split('_')
            if (len(split)== 1):
                dictAppear = getAllDictAppearance(mainID,rightDict)
                dictAverageKLScore = averageKLScore(dictAppear,dictKL_AllEntities,mainID, window)
                keep, remove = getIDToRemove(dictAverageKLScore)
                deleteOverlaptFromDict(dict,remove,window,mainID)

            print('zxc')





