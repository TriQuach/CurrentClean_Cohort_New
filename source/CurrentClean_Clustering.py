from source.KL_OneAttr_MultipleEntities import *

def isInTheSameCluster(key1,key2, cluster1, cluster2):
    if (key1 in cluster1 and key2 in cluster1):
        return True
    if (key1 in cluster2 and key2 in cluster2):
        return True
    return False

def CurreanClean_Clustering(threshold):
    listAttr = ['HR']
    dictEntitiesVal = normalizeDictArray(listAttr)
    listID = getAllEntitiesID(dictEntitiesVal)
    # listID = ['1','2','83','39']
    dictKL_AllEntities = getKLallEntities(dictEntitiesVal, listID, 'HR')

    cluster1 = [] # cluster that has values that are less than threshold
    cluster2 = []




    for key in dictKL_AllEntities:
        dictRight = dictKL_AllEntities[key]
        for key2 in dictRight:
            KLScore_1stWindow = dictRight[key2][0]
            if (KLScore_1stWindow < threshold):
                if (key not in cluster1):
                    if (isInTheSameCluster(key,key2,cluster1,cluster2) == False):
                        cluster1.append(key)
                        if (key in cluster2):
                            cluster2.remove(key)
                if (key2 not in cluster1):
                    if (isInTheSameCluster(key, key2, cluster1, cluster2) == False):
                        cluster1.append(key2)
                        if (key2 in cluster2):
                            cluster2.remove(key2)
                if (key in cluster2):
                    if (isInTheSameCluster(key, key2, cluster1, cluster2) == False):
                        cluster2.remove(key)
                if (key2 in cluster2):
                    if (isInTheSameCluster(key, key2, cluster1, cluster2) == False):
                        cluster2.remove(key2)
            else:
                if (key not in cluster1 and key not in cluster2):
                    cluster1.append(key)
                if (key2 not in cluster1 and key2 not in cluster2):
                    cluster2.append(key2)


    return cluster1,cluster2

def clusterOneWindow(array, threshold1, threshold2, threshold3, threshold4):
    cluster1 = []  # cluster that has values that are less than threshold
    cluster2 = []
    cluster3 = []
    cluster4 = []
    for i in range(len(array)):
        if (array[i] < threshold1):
            cluster1.append(str(i+2))
        elif (array[i] > threshold2 and array[i] < threshold3):
            cluster2.append(str(i+2))
        elif (array[i] > threshold4):
            cluster3.append(str(i + 2))
        else:
            cluster4.append(str(i+2))
    return cluster1, cluster2, cluster3, cluster4




def CurreanClean_Clustering_1stRound(threshold1, threshold2, threshold3, threshold4):
    listAttr = ['HR']
    dictEntitiesVal = normalizeDictArray(listAttr)
    listID = getAllEntitiesID(dictEntitiesVal)
    # listID = ['1','2','83','39']
    dictKL_AllEntities = getKLallEntities(dictEntitiesVal, listID, 'HR')




    dictRight = dictKL_AllEntities[listID[0]]

    array_2D_allWindow = []

    for key in dictRight:
        array_2D_allWindow.append(dictRight[key])
    array_2D_allWindow = np.asarray(array_2D_allWindow)

    resDict = {}
    for i in range(len(array_2D_allWindow[0])):
        window = array_2D_allWindow[:,i]
        cluster1, cluster2, cluster3, cluster4 = clusterOneWindow(window,threshold1,threshold2,threshold3,threshold4)
        cluster1.insert(0,listID[0])

        temp = {}
        temp["cohort1"] = cluster1
        temp["cohort2"] = cluster2
        temp["cohort3"] = cluster3
        temp["cohort4"] = cluster4

        currentWindow = "window_" + str(i)
        resDict[currentWindow] = temp


    return resDict



    # for key in dictRight:
    #     KLScore_1stWindow = dictRight[key][4]
    #     if (KLScore_1stWindow < threshold1):
    #         cluster1.append(key)
    #     elif (KLScore_1stWindow > threshold2 and KLScore_1stWindow < threshold3):
    #         cluster2.append(key)
    #     elif (KLScore_1stWindow > threshold4):
    #         cluster3.append(key)
    # return cluster1, cluster2, cluster3




threshold1 = 2.0
threshold2 = 8.0
threshold3 = 9.0
threshold4 = 19.0


print('---------*********---------')
print('lower threshold = ' + str(threshold1))
print('middle threshold = [' + str(threshold2) + "," + str(threshold3) + ']')

print('upper threshold = ' + str(threshold4))

print("CurrentClean-Cohort algorithm is running...")

print('---------*********---------')
resDict = CurreanClean_Clustering_1stRound(threshold1, threshold2,threshold3, threshold4)

print(resDict)

# print("cohort1")
# print((cluster1))
# print("---------*********---------")
# print('cohort2')
# print(cluster2)
# print("---------*********---------")
# print('cohort3')
# print(cluster3)


