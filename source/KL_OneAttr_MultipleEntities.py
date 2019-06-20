from source.Normalize import *
import source.constant as constant
def KL(P, Q):
    epsilon = 0.00001

    if (len(P) == 154 and len(Q) == 153):
        print("zxc")

    P = np.asarray(P, dtype=np.float)
    Q = np.asarray(Q, dtype=np.float)

    # You may want to instead make copies to avoid changing the np arrays.
    P = P + epsilon
    Q = Q + epsilon

    divergence = np.sum(P * np.log(P / Q))
    return abs(divergence)

def getKLbetween2Entities(dictEntitiesVal, IdLeft, IdRight, attr):
    arrHistoricaldValLeft = dictEntitiesVal[IdLeft][attr]
    arrHistoricalValRight = dictEntitiesVal[IdRight][attr]
    numElementEachWindow = int((len(arrHistoricaldValLeft) - 1) / constant.N_WINDOWS)
    step = 0
    arrEDScore = []
    for k in range(constant.N_WINDOWS):
        sliceArr1 = arrHistoricaldValLeft[step:(step + numElementEachWindow + 1)]
        sliceArr2 = arrHistoricalValRight[step:(step + numElementEachWindow + 1)]
        step += numElementEachWindow
        if (len(sliceArr1) == 154 and len(sliceArr2) == 153 ):
            print('zxczx')
        kl = KL(sliceArr1, sliceArr2)
        arrEDScore.append(kl)
    return arrEDScore

def getKLallEntities(dictEntitiesVal, listID, attr):
    dictRes = {}
    for i in range(len(listID)):
        dictKL_Score = {}
        for j in range(i+1, len(listID)):
            arrayKLscoreOnWindows = getKLbetween2Entities(dictEntitiesVal, listID[i], listID[j], attr)
            dictKL_Score[listID[j]] = arrayKLscoreOnWindows
        dictRes[listID[i]] = dictKL_Score

    return dictRes





listAttr = ['HR']
dictEntitiesVal = normalizeDictArray(listAttr)
listID = getAllEntitiesID(dictEntitiesVal)
x = getKLallEntities(dictEntitiesVal, listID, 'HR')
print(x)

