import matplotlib.pyplot as plt
from source.Score import *
from source.Normalize import *

n_windows = 10

def lineChartHistoricalVal():
    listID = ['11','14']
    listAttr = ['HR', 'SBP']
    res = get2DarrayOfValue(listID, listAttr)
    legend = []
    for key in res:
        arr = res[key]
        y = [i * 100 for i in arr]
        x = range(len(arr))
        plt.plot(x,y, marker = 'o', markerfacecolor='blue')
        legend.append('patient_' + key)
    plt.legend(legend)
    plt.show()

def lineChartOnWindows():
    listID = ['43']
    listAttr = ['HR', 'SBP']
    dictEntitiesVal = normalizeDictArray(listAttr)
    legend = []
    x = range(len(dictEntitiesVal['43'][listAttr[0]]))
    for key in listID:
        dict = dictEntitiesVal[key]
        for attr in listAttr:

            y = dict[attr]
            plt.plot(x, y)
            legend.append('patient_' + key + "_" + attr)
    numElementEachWindow = int((len(x) - 1) / n_windows)
    step = 0
    arr = []
    for i in range(n_windows):

        step += numElementEachWindow
        plt.axvline(x=step, linestyle="--", color='red')

    plt.legend(legend)
    plt.show()
    print("ad")

lineChartOnWindows()
