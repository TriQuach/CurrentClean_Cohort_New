import matplotlib.pyplot as plt

from source.Others.ChangeVolatility import *


#
# def lineChartHistoricalVal():
#     listID = ['11','14']
#     listAttr = ['HR', 'SBP']
#     res = get2DarrayOfValue(listID, listAttr)
#     legend = []
#     for key in res:
#         arr = res[key]
#         y = [i * 100 for i in arr]
#         x = range(len(arr))'
#         plt.plot(x,y, marker = 'o', markerfacecolor='blue')
#         legend.append('patient_' + key)
#     plt.legend(legend)
#     plt.show()

def lineChartOnWindows():
    # listID = ['72', '88', '98', '100', '66','22','43','93']
    listID = ['38','65','17','28']
    listAttr = ['HR']
    dictEntitiesVal = normalizeDictArray(listAttr)
    legend = []
    x = range(len(dictEntitiesVal[listID[0]][listAttr[0]]))
    for key in listID:
        dict = dictEntitiesVal[key]
        for attr in listAttr:
            x = range(len(dict[listAttr[0]]))
            y = dict[attr]
            plt.plot(x, y)
            legend.append('patient_' + key + "_" + attr)
    numElementEachWindow = int((len(x) - 1) / constant.N_WINDOWS)
    step = 0
    for i in range(constant.N_WINDOWS):

        step += numElementEachWindow
        plt.axvline(x=step, linestyle="--", color='red')

    plt.legend(legend)
    plt.show()
    print("ad")

def lineChartChangeVolatilityED():
    listID = ['40','49','76','99']
    listAttr = ['HR', 'SBP']
    euclidean = getVolatility(listAttr, constant.EUCLIDEAN)

    x = range(len(euclidean[listID[0]]))
    legend = []
    for key in listID:
        y = [i* 100 for i in euclidean[key]]
        plt.plot(x,y, marker = 'o', markerfacecolor='blue')
        legend.append('patient_' + key)
    plt.legend(legend)
    plt.xlabel("window")
    plt.ylabel("ED between ChangeVolatility of HR and SBP")

    plt.show()

def lineChartChangeVolatilityCosine():
    listID = ['5','20','34','58']
    cosine = getVolatility(listAttr, constant.COSINE)
    x = range(len(cosine[listID[0]]))
    legend = []
    for id in listID:
        arrNested = cosine[id]
        arr = []
        for i in range(len(arrNested)):
           arr.append(arrNested[i][0][0])
        y = [i * 100 for i in arr]
        plt.plot(x, y, marker = 'o', markerfacecolor='blue')
        legend.append('patient_' + id)
    plt.legend(legend)
    plt.xlabel("window")
    plt.ylabel("Cosine between ChangeVolatility of HR and SBP")

    plt.show()




lineChartOnWindows()