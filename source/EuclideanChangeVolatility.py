import numpy as np
from scipy.spatial import distance

from source.Entity import *

def getChangeVector(arr):
    res = []
    for i in range(len(arr) - 1):
        res.append(abs(arr[i+1] - arr[i]))
    return res

def getDistanceVector(listID, listAttr):
    dictEntitiesVal = creatDictArrayOfAttr("../data/mimic_half.txt")
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

def getDistanceBetweenVectors(listID, listAttr):
    res = getDistanceVector(listID, listAttr)
    arr = []
    sum = 0
    resDict = {}
    for id in listID:
        dict = res[id]

        for attr in listAttr:
            arr.append(dict[attr])

        for i in range(len(arr) - 1):
            dist = distance.euclidean(arr[i], arr[i+1])
            resDict[id] = dist
        arr = []
    return resDict


listID = ['1','77']
listAttr = ['HR', 'SBP']
res = getDistanceBetweenVectors(listID,listAttr)

print("asd")
