# Code
import matplotlib.pyplot as plt
import random as rand
import numpy as np
import filledflies as ff

def multipleruns(numberofruns, numberofflies, numberofdays, temperaturefrequencyarray, meantemp, per, gain, initvariabilityarray, driftvariabilityarray, heritabilityarray):
    bigarray=np.zeros((numberofruns, numberofdays, 2))
    variabilityarray=np.zeros((numberofruns, numberofdays))
    driftarray=np.zeros((numberofruns, numberofdays))
    mean=np.zeros((numberofdays))

    fig=plt.figure(figsize=(6,6))
    colors=['lightgray','lightgreen']
    colorsi=['gray','green']
    x=np.arange(0,numberofdays)
    tempdata=np.zeros([2,numberofdays])

    for i in range(0,2):
        for n in range(0,numberofruns):

            tempdata[i,:]=gain[i]*np.sin(x*2*np.pi/per[i]+182*2*np.pi)+meantemp[i]
            [fliesmatrix,flyarray]=ff.filledflies(numberofflies,100,4,tempdata[i,:],5,initvariabilityarray[i],driftvariabilityarray[i],per[i], gain[i])
            bigarray[n,:,i]=flyarray
        for f in range(0, fliesmatrix.shape[0]):
            plt.plot (fliesmatrix[f,:,2], colors[i], lw=.4)
        plt.plot(np.nanmean(fliesmatrix[:,:,2],axis=0),colorsi[i])

    plt.title ('Fly Preferences')
    plt.xlabel ('Days')
    plt.ylabel ('Fly Preferences')

    plt.show()

    for o in range (0,2):
        plt.plot(x, tempdata[o,:], colors[o])
    plt.ylabel('Temperature')
    plt.axis('tight')
    plt.show()
    plt.title ('Number of Flies per Day')
    plt.xlabel ('Days')
    for i in range(0,2):
        for n in range(0,numberofruns):
            plt.plot (bigarray[n,:,i], colors[i], lw=.4)
            for q in range(numberofdays):
                meanflies=(np.sum(bigarray[:,q,i]))/numberofruns
                mean[q]=meanflies
            plt.plot(mean,colorsi[i])

    plt.show()
    print('Bigarray size')
    print(bigarray.shape)
