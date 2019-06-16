import numpy as np
from scipy.spatial import distance
import source.constant as constant
from source.Normalize import *
from sklearn.metrics.pairwise import cosine_similarity
import operator

n_windows = 10

def getChangeVector(arr):
    res = []
    for i in range(len(arr) - 1):
        res.append(abs(arr[i+1] - arr[i]))
    return res

def getDistanceVector(listAttr):
    dictEntitiesVal = normalizeDictArray( listAttr)
    listID = getAllEntitiesID(dictEntitiesVal)
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

def getVolatility(listAttr, type):
    res = getDistanceVector(listAttr)
    listID = getAllEntitiesID(res)
    arr = []
    sum = 0
    resDict = {}
    for id in listID:
        dict = res[id]

        for attr in listAttr:
            arr.append(dict[attr])
        numElementEachWindow = int((len(arr[0]) - 1) / n_windows)
        step = 0
        arrEDScore = []
        for i in range(len(arr) - 1):
            if (type == constant.EUCLIDEAN):
                for k in range(n_windows):
                    sliceArr1 = arr[i][step:(step + numElementEachWindow + 1)]
                    sliceArr2 = arr[i+1][step:(step + numElementEachWindow + 1)]
                    step += numElementEachWindow
                    dist = distance.euclidean(sliceArr1, sliceArr2)
                    arrEDScore.append(dist)
                sliceArr1 = arr[i][step: len(arr[0])]
                sliceArr2 = arr[i+1][step: len(arr[0])]
                dist = distance.euclidean(sliceArr1, sliceArr2)
                arrEDScore.append(dist)

            # else:
            #     arr[i] = [arr[i]]
            #     arr[i+1] = [arr[i+1]]
            #     dist = cosine_similarity(arr[i], arr[i+1])
            resDict[id] = arrEDScore
        arr = []
    return resDict

def sortDict(dict):
    sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
    return sorted_x


listID = ['1','77']
listAttr = ['HR', 'SBP']


print("Euclidean distance:")
euclidean = getVolatility(listAttr, constant.EUCLIDEAN)
print(euclidean)

# '11': [0.3067958701721019, 0.3182699411082869, 0.31629004613110945, 0.01699251624552131],
# '14': [0.3064969711381844, 0.28892113176415246, 0.30322267818374943, 0.025387668846560185],
# '76': [0.4610121365149762, 0.45844314272324055, 0.4730181082878332, 0.0],
# '67': [0.46270322590448276, 0.47481621482348424, 0.4918891118815509, 0.0],
# '5': [0.17458736116892956, 0.18710077356453067, 0.22183278443295068, 0.0]
# '2': from window 6->7
# print("Sorting...")
# print(sortDict(euclidean))
# print("*-----------------*")
#
# print("Cosine Similarity:")
# cosine = getVolatility(listAttr, constant.COSINE)
# print(cosine)




