
import numpy as np
import copy
from operator import attrgetter
import random
import source.Others.constant as constant

class Cell:
    def __init__(self, timestamp, dirty, label, truth, isLabel):
        self.timestamp = timestamp
        self.dirty = dirty
        self.label = label
        self.truth = truth
        self.isLabel = isLabel

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

def createLabel_value(attribute):
    if (attribute == constant.HR):
        return



def checkGroundTruth(attribute, value):
    isLabel = bool(random.getrandbits(1))
    if (attribute == constant.WT):
        truth = random.uniform(0.0, 200.0)
        if (isLabel == True):
            return truth,truth,True
        else:
            return value,truth, False
    elif (attribute == constant.LDL):
        truth = random.uniform(100.0, 159.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.HDL):
        truth = random.uniform(35.0, 80.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.HR):
        truth = random.uniform(60.0, 100.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.DBP):
        truth = random.uniform(0.0, 89.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.SBP):
        truth = random.uniform(0.0, 139.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.CVP):
        truth = random.uniform(3.0, 8.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.RR):
        truth = random.uniform(12.0, 20.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.SpO2):
        truth = random.uniform(94.0, 100.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.TMP):
        truth = random.uniform(36.5, 37.5)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.APH):
        truth = random.uniform(7.35, 7.45)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.Hb):
        truth = random.uniform(120.0, 160.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.RBC):
        truth = random.uniform(4.0, 5.1)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.WBC):
        truth = random.uniform(4.0, 11.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.MONO):
        truth = random.uniform(0.2, 1.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.EOS):
        truth = random.uniform(0.0, 6.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.LY):
        truth = random.uniform(1.0, 3.5)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.RDW):
        truth = random.uniform(11.0, 14.5)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    elif (attribute == constant.ABE or attribute == constant.ACO2 or attribute == constant.TC or attribute == constant.RBCF):
        truth = random.uniform(0.0, 1.0)
        if (isLabel == True):
            return truth, truth, True
        else:
            return value, truth, False
    # ABE, ACO2, TC, RBCF
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
                label, truth, isLabel = checkGroundTruth(attributeName,attributeValue)
                name = ID + '_' + attributeName
                objCell = Cell(Timestamp,attributeValue,label,truth,isLabel)
                if (count == 0):
                        arrayAttributes.append(attributeName)
                if (ID not in dictEntitiesVal):
                    dict = {}
                    arr = []
                    arr.append(objCell)
                    dict[attributeName] = arr
                    dictEntitiesVal[ID] = dict


                else:
                    dict2 = dictEntitiesVal[ID]
                    if (attributeName not in dict2):
                        arr2 = []
                        arr2.append(objCell)
                        dict2[attributeName] = arr2
                        dictEntitiesVal[ID] = dict2
                    else:
                        arr2 = dict2[attributeName]
                        arr2.append(objCell)
                        dict2[attributeName] = arr2
                        dictEntitiesVal[ID] = dict2
        count += 1

    return dictEntitiesVal

def getAllEntitiesID(dict):
    res = []
    for key in dict:
        res.append(key)
    return res

def writeFile(dictEntitiesVal):


    for id in dictEntitiesVal:
        for attr in dictEntitiesVal[id]:
            filename = "/Users/triquach/Documents/CurrentClean_CohortNew/data/Cell_Series/" + id + '_' + attr + '.txt'
            f2 = open(filename, "w+")
            arr = dictEntitiesVal[id][attr]
            for obj in arr:
                f2.write(str(obj.timestamp))
                f2.write(',')
                f2.write(str(obj.dirty))
                f2.write(',')
                f2.write(str(obj.label))
                f2.write(',')
                f2.write(str(obj.truth))
                f2.write(',')
                f2.write(str(obj.isLabel))
                f2.write('\n')

            f2.close()

def modify1stObja(dictEntitiesVal):
    for entity in dictEntitiesVal:
        for attr in dictEntitiesVal[entity]:
            firstObj = dictEntitiesVal[entity][attr][0]
            firstObj.isLabel = True
            firstObj.label = firstObj.truth
            dictEntitiesVal[entity][attr][0] =firstObj

def temp(dictEntitiesVal):
    arr = []
    temp = dictEntitiesVal['1']
    for attr in temp:
        arr.append(attr)
    return arr

dictEntitiesVal = creatDictArrayOfAttr('/Users/triquach/Documents/CurrentClean_CohortNew/data/Mimic100_3.txt')
modify1stObja(dictEntitiesVal)
writeFile(dictEntitiesVal)
arr = temp(dictEntitiesVal)
print(arr)





