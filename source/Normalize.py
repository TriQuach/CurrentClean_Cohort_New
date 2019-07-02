from source.Entity import *

def normalizeDictArray(listAttr):
    dict = creatDictArrayOfAttr("../data/mimic_20.txt")
    listID = getAllEntitiesID(dict)
    dict_normalized = copy.deepcopy(dict)
    for key in listID:
        dictArray = dict_normalized[key]
        for attrName in listAttr:

            arr = dictArray[attrName]

            temp_norm = [float(i) / max(arr) for i in arr]
            # lower, upper = 1.0, 100.0
            # norm = [lower + (upper - lower) * x for x in temp_norm]
            dictArray[attrName] = temp_norm
        dict_normalized[key] = dictArray
    return dict_normalized

