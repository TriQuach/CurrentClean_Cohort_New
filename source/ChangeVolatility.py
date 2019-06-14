import numpy as np
from scipy.spatial import distance
import source.constant as constant
from source.Normalize import *
from sklearn.metrics.pairwise import cosine_similarity
def getChangeVector(arr):
    res = []
    for i in range(len(arr) - 1):
        res.append(abs(arr[i+1] - arr[i]))
    return res

def getDistanceVector(listID, listAttr):
    dictEntitiesVal = normalizeDictArray(listID, listAttr)
    dictRes = {}
    for id in listID:
        dict = dictEntitiesVal[id]
        dict_temp = {}
        for attr in listAttr:
            arr = dict[attr]
            vector = getChangeVector(arr)
            dict_temp[attr] = vector
        dictRes[id] = dict_temp
    return dictRes

def getVolatility(listID, listAttr, type):
    res = getDistanceVector(listID, listAttr)
    arr = []
    sum = 0
    resDict = {}
    for id in listID:
        dict = res[id]

        for attr in listAttr:
            arr.append(dict[attr])

        for i in range(len(arr) - 1):
            if (type == constant.EUCLIDEAN):
                dist = distance.euclidean(arr[i], arr[i+1])
            else:
                arr[i] = [arr[i]]
                arr[i+1] = [arr[i+1]]
                dist = cosine_similarity(arr[i], arr[i+1])
            resDict[id] = dist
        arr = []
    return resDict



listID = ['1','77']
listAttr = ['HR', 'SBP']


print("Euclidean distance:")
euclidean = getVolatility(listID,listAttr, constant.EUCLIDEAN)
print(euclidean)

print("*-----------------*")

print("Cosine Similarity:")
cosine = getVolatility(listID,listAttr, constant.COSINE)
print(cosine)




