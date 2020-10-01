#Master Code

import numpy as np
import matplotlib.pyplot as plt
import random as rand

def filledflies(numberofflies, flyHP, dailyHPchange, tempdata, matureAge, initvariability, driftvariability, per, gain, firstday=1, flynerals=True):
    "This function needs initial # of flies, number of days, the fly's hit points, and increments the HP goes down by each day"
    newflyHP=flyHP
    flybuffer=numberofflies*2
    numdimensions=3
#     global numberofdays
    numberofdays=tempdata.shape[0]
#     global fliesmatrix
    fliesmatrix=np.zeros((flybuffer, numberofdays, numdimensions))
    fliesmatrix[:,:,:]=np.nan
    fliesmatrix[0:numberofflies,0,0]=newflyHP
    fliesmatrix[0:numberofflies,0,1]=firstday
    fliesmatrix[0:numberofflies,0,2]=np.random.normal(0,initvariability,numberofflies)*initvariability
    numberofdeadflies=0
    newbornflies=0
    matureAge=10
    flyHP=100
#     global flyarray
#     global t
    gain=8.5
    per=365
    flyarray=np.zeros([numberofdays])
    initvararray=np.zeros([numberofdays])
    driftvararray=np.zeros([numberofdays])
    flyarray[0]=numberofflies
    for t in range(1, numberofdays):
        for f in range(0, numberofflies):
            fliesmatrix[f,t,2]=fliesmatrix[f,t-1,2]
#             if f>21:
                #print(fliesmatrix[f,t-1,2])
#             print(fliesmatrix[f,t,2])
            effectivetemp=tempdata[t]-fliesmatrix[f,t,2]+initvariability/2
            if (fliesmatrix[f,t-1,1]!=np.nan) & (fliesmatrix[f,t-1,1]<10):
                matureHit=matureAge/(0.2306*effectivetemp*effectivetemp-11.828*effectivetemp+158.34+1)
                q=fliesmatrix[f,t-1,1]
                fliesmatrix[f,t,1]=fliesmatrix[f,t-1,1]+matureHit
                if fliesmatrix[f,t,1]>=10:
                    fliesmatrix[f,t,2]=np.random.normal()*initvariability
            if fliesmatrix[f,t-1,1]>=10:
                matureHit=matureAge/(0.2306*effectivetemp*effectivetemp-11.828*effectivetemp+158.34+1)
                fliesmatrix[f,t,1]=fliesmatrix[f,t-1,1]+matureHit
                fliesmatrix[f,t,2]=fliesmatrix[f,t,2]+(np.random.normal()-.5)*driftvariability
#                 print(fliesmatrix[f,:,2])
            HPHit=flyHP/(0.4074*effectivetemp*effectivetemp-28.356*effectivetemp+506.2)
            if fliesmatrix[f,t-1,0]>HPHit: # Does Fly die
                fliesmatrix[f,t,0]=fliesmatrix[f,t-1,0]-HPHit
            else:
                fliesmatrix[f,t:,:]=np.nan
            if (np.random.random_sample() < .0203):
                fliesmatrix[f,t:,:]=np.nan
#             print(fliesmatrix[f,t,0])
#             print(fliesmatrix[f,t-1,0])
            if (np.isnan(fliesmatrix[f,t,0]))&(fliesmatrix[f,t-1,0]!=np.nan):
#                print("Fly " +str(f+1) + " died on day " +str(t+1))
                fliesmatrix[f,t:,:]=np.nan
                numberofdeadflies=numberofdeadflies+1
                numberofflies=numberofflies-1
            if (fliesmatrix[f,t,1]>=matureAge) & (np.random.random_sample() < .366) & (fliesmatrix[f,t,0]!=0):
                fliesmatrix[numberofflies,t,0]=newflyHP
                fliesmatrix[numberofflies,t,2]=fliesmatrix[f,t,2]
                if newflyHP<=0:
                    break
                newbornflies=newbornflies+1
                numberofflies=numberofflies+1
            if numberofflies==flybuffer:
                extrabuffer=np.zeros((20,numberofdays, numdimensions))
                extrabuffer[:,:,:]=np.nan
                fliesmatrix=np.vstack((fliesmatrix, extrabuffer))
                flybuffer=flybuffer+20
        flyarray[t]=numberofflies
        initvararray[t]=initvariability
        driftvararray[t]=driftvariability
#         global flies
        flies=flyarray[t]
#         print(flies)
        
#     fig=plt.figure(figsize=(8,8))
#     #fig.add_subplot(1,2,1)
#     plt.subplot(2,100,(1,45))
#     for f in range(0, fliesmatrix.shape[0]):
#         plt.plot (fliesmatrix[f,:,2])
#     plt.title ('Fly Preferences thoughout the Days')
#     plt.xlabel ('Days')
#     plt.ylabel ('Fly Preferences')

#     plt.subplot(2,100,(103,150))
#     plt.title ('Effective Temperature Over Time')
#     plt.xlabel ('Days')
#     plt.ylabel ('Effective Temperature')
#     fliesmatrix[:,:,2]=fliesmatrix[:,:,2]+tempdata[t]
#     for f in range(0, fliesmatrix.shape[0]):
#         plt.plot(fliesmatrix[f,:,2])
        
#     plt.subplot(2,100,(55,99))
#     plt.plot (flyarray, 'gray')
#     plt.title ('Number of Flies per Day')
#     plt.xlabel ('Days')
#     plt.ylabel ('Flies')
    
#     print("A total of "+str(numberofdeadflies)+" flies died in this simulation.")
#     print("A total of "+str(newbornflies)+" flies were born in this simulation!")
    return fliesmatrix, flyarray;
