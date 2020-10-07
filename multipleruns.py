# Code
import matplotlib.pyplot as plt
import random as rand
import numpy as np
import filledflies as ff

def multipleruns(numberofruns, numberofflies, numberofdays, temperaturefrequencyarray, meantemp, per, gain, initvariabilityarray, driftvariabilityarray, heritabilityarray):
#     plt.title ('Number of Flies per Day')
#     plt.xlabel ('Days')
#     plt.ylabel ('Flies')
    bigarray=np.zeros((numberofruns, numberofdays, 2))
    variabilityarray=np.zeros((numberofruns, numberofdays))
    driftarray=np.zeros((numberofruns, numberofdays))
    mean=np.zeros((numberofdays))

    fig=plt.figure(figsize=(6,6))
#     fig.add_subplot(1,2,1)
    colors=['lightgray','lightgreen']
    colorsi=['gray','green']
    x=np.arange(0,numberofdays)
    tempdata=np.zeros([2,numberofdays])

    for i in range(0,2):
        for n in range(0,numberofruns):

#         plt.subplot(2,100,(1,45))
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

    # fig=plt.figure(figsize=(8,8))
    # colors=['pink','orange']

    # plt.subplot(2,100,(103,150))
    for o in range (0,2):
        plt.plot(x, tempdata[o,:], colors[o])
    plt.ylabel('Temperature')
    plt.axis('tight')
    plt.show()
    # plt.subplot(2,100,(55,99))
    plt.title ('Number of Flies per Day')
    plt.xlabel ('Days')
#     plt.ylabel ('Flies')
    for i in range(0,2):
        for n in range(0,numberofruns):
        # ff.filledflies(10,100,4,tempdata,5,0,4,365,8.5)
#         bigarray=np.full((1,numberofdays),flyarray)
#         flyarray[0]=numberofflies
            plt.plot (bigarray[n,:,i], colors[i], lw=.4)
        # bigarray[i]=flyarray
#     print(bigarray)
            for q in range(numberofdays):
                meanflies=(np.sum(bigarray[:,q,i]))/numberofruns
                mean[q]=meanflies
#     print(mean)
            plt.plot(mean,colorsi[i])
    plt.show()
    print('Bigarray size')
    print(bigarray.shape)
