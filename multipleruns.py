def multipleruns(numberofdays, numberofflies, numberofruns, temperaturefrequencyarray, per, gain, initvariabilityarray, driftvariabilityarray, heritabilityarray):
#     plt.title ('Number of Flies per Day')
#     plt.xlabel ('Days')
#     plt.ylabel ('Flies')
    bigarray=np.zeros((numberofruns, numberofdays))
    variabilityarray=np.zeros((numberofruns, numberofdays))
    driftarray=np.zeros((numberofruns, numberofdays))
    mean=np.zeros((numberofdays))

    fig=plt.figure(figsize=(6,6))
#     fig.add_subplot(1,2,1)
    colors=['lightgray','lightgreen']
    colorsi=['gray','green']
    for i in range(0,2):
#         plt.subplot(2,100,(1,45))
        [fliesmatrix,flyarray]=filledflies(10,100,4,tempdata,5,initvariabilityarray[i],driftvariabilityarray[i],per[i], gain[i])
        for f in range(0, fliesmatrix.shape[0]):
            plt.plot (fliesmatrix[f,:,2], colors[i])
            plt.plot(np.nanmean(fliesmatrix[:,:,2],axis=0),colorsi[i])
        plt.title ('Fly Preferences')
        plt.xlabel ('Days')
        plt.ylabel ('Fly Preferences')
        plt.show()
    
    fig=plt.figure(figsize=(8,8))
    colors=['pink','orange']
    x=np.arange(0,365)
    plt.subplot(2,100,(103,150))
    for o in range (0,2):
        temparray=gain[o]*np.sin(x*2*np.pi/per[o]+182*2*np.pi)+15.5
        plt.plot(x, temparray, colors[o])
    plt.ylabel('Temperature')
    plt.axis('tight')
        
    plt.subplot(2,100,(55,99))
    plt.title ('Number of Flies per Day')
    plt.xlabel ('Days')
#     plt.ylabel ('Flies')
    
    for i in range(numberofruns):
        filledflies(10,100,4,tempdata,5,0,4,365,8.5)
#         bigarray=np.full((1,numberofdays),flyarray)
#         flyarray[0]=numberofflies
        plt.plot (flyarray, 'pink')
        bigarray[i]=flyarray
#     print(bigarray)
    for q in range(numberofdays):
        meanflies=(np.sum(bigarray[:,q]))/numberofruns
        mean[q]=meanflies
#     print(mean)
    plt.plot(mean,'red')
        
