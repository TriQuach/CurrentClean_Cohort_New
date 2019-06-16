
import numpy as np
import copy
from operator import attrgetter
fiveEntities = ["Marco-Etcheverry","Carlos-Valderrama","Eric-Wynalda","Preki","Robert-Warzycha"]


class Entity(object):
    pass

def creatDict(fileName):
    dictEntities = {}
    arrayAttributes = []
    f = open(fileName, "r")
    count = 0
    for line in f:
        word = line.split(',')
        obj = Entity()
        for i in range(len(word)):
            if (i != 0 and i != 1):

                attributeName = word[i].split(":")[0]
                attributeValue = word[i].split(":")[1]
                setattr(obj,attributeName,attributeValue)
                if (count == 0):
                    arrayAttributes.append(attributeName)
        setattr(obj,"Timestamp",word[0])
        setattr(obj,"ID", word[1])
        ID = getattr(obj,"ID")
        if (ID not in dictEntities):
            arrObjects = []
            arrObjects.append(obj)
            dictEntities[ID] = arrObjects
        else:
            arr = dictEntities[ID]
            arr.append(obj)
            dictEntities[ID] = arr
        count += 1
    return arrayAttributes, dictEntities

def getDictOfArrayForEachAttr(arrEntities,arrayAttributes):
    dict = {}
    for entity in arrEntities:
        for attr in arrayAttributes:
            val = float(getattr(entity,attr))
            if (attr not in dict):
                arrVal = []
                arrVal.append(val)
                dict[attr] = arrVal
            else:
                arrVal = dict[attr]
                arrVal.append(val)
                dict[attr] = arrVal
    return dict

def normalize(arrayAttributes, dictEntities):
    clone_dict = copy.deepcopy(dictEntities)
    for key in clone_dict:
        arr = clone_dict[key]
        dictArrayVal = getDictOfArrayForEachAttr(arr, arrayAttributes)
        for entity in arr:
            for key2 in dictArrayVal:
                maxVal = max(dictArrayVal[key2])
                current_val = float(getattr(entity,key2))
                normalized_val = float(current_val / maxVal )
                setattr(entity,key2,normalized_val)

    return clone_dict



def creatDictArrayOfAttr(fileName):
    dictEntitiesVal = {}
    arrayAttributes = []
    f = open(fileName, "r")
    count = 0
    for line in f:
        word = line.split(',')
        obj = Entity()
        ID = word[1]
        Timestamp = word[0]
        for i in range(len(word)):

            if (i != 0 and i != 1):
                attributeName = word[i].split(":")[0]
                attributeValue = float(word[i].split(":")[1])
                if (count == 0):
                        arrayAttributes.append(attributeName)
                if (ID not in dictEntitiesVal):
                    dict = {}
                    arr = []
                    arr.append(attributeValue)
                    dict[attributeName] = arr
                    dictEntitiesVal[ID] = dict


                else:
                    dict2 = dictEntitiesVal[ID]
                    if (attributeName not in dict2):
                        arr2 = []
                        arr2.append(attributeValue)
                        dict2[attributeName] = arr2
                        dictEntitiesVal[ID] = dict2
                    else:
                        arr2 = dict2[attributeName]
                        arr2.append(attributeValue)
                        dict2[attributeName] = arr2
                        dictEntitiesVal[ID] = dict2
        count += 1

    return dictEntitiesVal

def getAllEntitiesID(dict):
    res = []
    for key in dict:
        res.append(key)
    return res









