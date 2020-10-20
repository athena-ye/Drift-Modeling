#Master Code

import numpy as np
import matplotlib.pyplot as plt
import random as rand
import scipy.stats as stat
import time

def filledflies(numberofflies, flyHP, dailyHPchange, tempdata, matureAge, initvariability, driftvariability, per, gain, firstday=1, flynerals=True):
    "This function needs initial # of flies, number of days, the fly's hit points, and increments the HP goes down by each day"
    newflyHP=flyHP
    flybuffer=numberofflies*10
    numdimensions=3
    birthprob=.0366 # Birthprob .366 from previous code
    deathprob=.0203 # Odds of death from random chance. .0203 from previous codes
    numberofdays=tempdata.shape[0]
    fliesmatrix=np.zeros((flybuffer, numberofdays, numdimensions))
    fliesmatrix[:,:,:]=np.nan
    fliesmatrix[0:numberofflies,0,0]=newflyHP # Dimension keeping track of flyHP
    fliesmatrix[0:numberofflies,0,1]=firstday # Dimension keeping track of age
    fliesmatrix[0:numberofflies,0,2]=np.random.normal(0,initvariability,numberofflies) # Dimensions keeping track of drift
    numberofdeadflies=0
    newbornflies=0
    matureAge=10
    flyHP=100
    gain=8.5
    per=365
    flyarray=np.zeros([numberofdays])
    initvararray=np.zeros([numberofdays])
    driftvararray=np.zeros([numberofdays])
    flyarray[0]=numberofflies
    for t in range(1, numberofdays):
        tic = time.perf_counter()
        for f in range(0, numberofflies):
            if fliesmatrix[f,t,2]!=np.nan:
                fliesmatrix[f,t,2]=fliesmatrix[f,t-1,2]
                effectivetemp=tempdata[t]-fliesmatrix[f,t,2]
                matureHit=matureAge/(0.2306*effectivetemp*effectivetemp-11.828*effectivetemp+158.34+1) # From Cain et al.
                if (fliesmatrix[f,t-1,1]!=np.nan) & (fliesmatrix[f,t-1,1]<10): 
                    fliesmatrix[f,t,1]=fliesmatrix[f,t-1,1]+matureHit
                    if fliesmatrix[f,t,1]>=10:
                        fliesmatrix[f,t,2]=np.random.normal(0, initvariability)
                if fliesmatrix[f,t-1,1]>=10:
                    fliesmatrix[f,t,1]=fliesmatrix[f,t-1,1]+matureHit
                    fliesmatrix[f,t,2]=metropolishastingsdrift(fliesmatrix[f,t,2], driftvariability)
                HPHit=flyHP/(0.4074*effectivetemp*effectivetemp-28.356*effectivetemp+506.2)
                if (np.random.random_sample() < deathprob) & (not np.isnan(fliesmatrix[f,t-1,2])): # Fly dies due to random chance
                    fliesmatrix[f,t:,:]=np.nan
                    numberofdeadflies=numberofdeadflies+1
                elif fliesmatrix[f,t-1,0]>HPHit: # Daily subtraction of HPHit
                    fliesmatrix[f,t,0]=fliesmatrix[f,t-1,0]-HPHit
                elif (fliesmatrix[f,t-1,0]<HPHit) & (fliesmatrix[f,t-1,0]>0) & (fliesmatrix[f,t,2] != np.nan): # Fly dies due to HPHit
                    fliesmatrix[f,t:,:]=np.nan
                    numberofdeadflies=numberofdeadflies+1
                if (np.isnan(fliesmatrix[f,t,0]))&(fliesmatrix[f,t-1,0]!=np.nan): # Change status of fly to dead
                    fliesmatrix[f,t:,:]=np.nan
                if (fliesmatrix[f,t,1]>=matureAge) & (np.random.random_sample() < birthprob): # Birth of a fly!
                    newbornflies=newbornflies+1
                    fliesmatrix[numberofflies,t,0]=newflyHP
                    fliesmatrix[numberofflies,t,1]=firstday
                    fliesmatrix[numberofflies,t,2]=fliesmatrix[f,t,2]
                    # if newflyHP<=0: # when would newflyHP be less than 0?
                    #     break
                    numberofflies=numberofflies+1
                if numberofflies==flybuffer: # Used to extend flybuffer if numberofflies exceeds the space given
                    extrabuffer=np.zeros((20,numberofdays, numdimensions))
                    extrabuffer[:,:,:]=np.nan
                    fliesmatrix=np.vstack((fliesmatrix, extrabuffer))
                    flybuffer=flybuffer+20
        flyarray[t]=numberofflies-numberofdeadflies # Needed for the fly mean in multipleruns function
        toc = time.perf_counter()
    return fliesmatrix, flyarray;

def metropolishastingsdrift(currentvalue, variability):
    #randomly drift using metropolishastings to avoid too much of a difference
    percentdrift=.2
    pcurrentvalue=stat.norm.pdf(currentvalue,0,variability)
    # proposedvalue=np.random.normal(0,variability)
    proposedvalue=np.random.normal(currentvalue,variability*percentdrift)

    pproposedvalue=stat.norm.pdf(proposedvalue,0,variability)
    if pproposedvalue/pcurrentvalue>(1-np.random.rand()):
        # return proposedvalue*percentdrift+currentvalue*(1-percentdrift)
        return proposedvalue
    else:
        return currentvalue
