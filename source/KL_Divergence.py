from scipy import stats
import numpy as np
import pandas as pd
from source.Normalize import *

def KL(P, Q):
    epsilon = 0.00001

    P = np.asarray(P, dtype=np.float)
    Q = np.asarray(Q, dtype=np.float)

    # You may want to instead make copies to avoid changing the np arrays.
    P = P + epsilon
    Q = Q + epsilon

    divergence = np.sum(P * np.log(P / Q))
    return abs(divergence)


def getKLDistance(listID, listAttr):
    dictEntitiesVal = normalizeDictArray(listID, listAttr)
    arr = []
    resDict = {}
    for id in listID:
        tempDict = dictEntitiesVal[id]
        for attr in listAttr:
            arr.append(tempDict[attr])
        for i in range(len(arr)-1):
            kl = KL(arr[i],arr[i+1])
        resDict[id] = kl
        arr = []

    return resDict


listID = ['1','77']
listAttr = ['HR', 'SBP']
resDict = getKLDistance(listID,listAttr)
print("KL_Divergence:")
print(resDict)