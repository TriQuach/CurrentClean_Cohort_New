from source.Entity.Normalize import *
from source.Entity.Entity import *

n_windows = 10

def KL(P, Q):
    epsilon = 0.00001

    P = np.asarray(P, dtype=np.float)
    Q = np.asarray(Q, dtype=np.float)

    # You may want to instead make copies to avoid changing the np arrays.
    P = P + epsilon
    Q = Q + epsilon

    divergence = np.sum(P * np.log(P / Q))
    return abs(divergence)


def getKLDistance( listAttr):
    dictEntitiesVal = normalizeDictArray( listAttr)
    listID = getAllEntitiesID(dictEntitiesVal)
    arr = []
    resDict = {}
    for id in listID:
        tempDict = dictEntitiesVal[id]
        for attr in listAttr:
            arr.append(tempDict[attr])
        numElementEachWindow = int((len(arr[0]) - 1) / n_windows)
        step = 0
        arrEDScore = []
        for i in range(len(arr)-1):
            for k in range(n_windows):
                sliceArr1 = arr[i][step:(step + numElementEachWindow + 1)]
                sliceArr2 = arr[i + 1][step:(step + numElementEachWindow + 1)]
                step += numElementEachWindow
                kl = KL(sliceArr1, sliceArr2)
                arrEDScore.append(kl)
            sliceArr1 = arr[i][step: len(arr[0])]
            sliceArr2 = arr[i + 1][step: len(arr[0])]
            dist = KL(sliceArr1, sliceArr2)
            arrEDScore.append(dist)

        resDict[id] = arrEDScore
        arr = []

    return resDict


listAttr = ['HR', 'SBP']
print("KL_Divergence:")
resDict = getKLDistance(listAttr)

# '1' - '38', '39

print(resDict)