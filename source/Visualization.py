import matplotlib.pyplot as plt
from source.Score import *

def lineChartHistoricalVal():
    listID = ['1', '77','2','3','4','5']
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

lineChartHistoricalVal()
