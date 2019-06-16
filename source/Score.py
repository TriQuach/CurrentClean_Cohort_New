from source.Normalize import *
import numpy as np

n_windows = 10

def getDistance(arr):
    arr = np.asarray(arr)
    res = []
    for i in range(len(arr[0])):
        col = arr[:,i]
        sum = 0
        for j in range(len(col)-1):
            dis = abs(col[j+1] - col[j])
            sum += dis
        res.append(sum)


    return res

def getScoreBasedOnWindow( arr, n_windows):
    numElementEachWindow = int((len(arr) - 1) / n_windows)
    step = 0
    res = []
    for i in range(n_windows):
        sliceArr = arr[step:(step + numElementEachWindow + 1)]
        res.append(np.mean(sliceArr))
        step += numElementEachWindow
    sliceArr = arr[step : len(arr)]
    res.append(np.mean(sliceArr))
    return res




def get2DarrayOfValue(listID, listAttr):
    dict_normalized = normalizeDictArray( listAttr)
    res = {}
    for id in listID:
        arr = []
        dictArrVal = dict_normalized[id]
        for attr in listAttr:
            arr.append(dictArrVal[attr])
        arrayDistance = getDistance(arr)
        scoreForOneEntity = getScoreBasedOnWindow(arrayDistance, n_windows)
        res[id] = scoreForOneEntity
    return res

def getOverallScore(dict):
    resDict = {}
    for key in dict:
        arr = dict[key]
        resDict[key] = np.mean(arr)
    return resDict
# #
listID = ['1','77']
listAttr = ['HR', 'SBP']

res = getOverallScore(get2DarrayOfValue(listID,listAttr))

print(res)