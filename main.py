import math
import numpy as np
import scipy.stats
from scipy.stats import entropy
from scipy.misc import derivative
GLOBAL_COUNT, LOCAL_COUNT, RANDOM_COUNT, CONSTANT_COUNT, ODD_COUNT=0,0,0,0,0
# As of now we have taken and estimated the values based on N=100


def entropy_x(values, N):
    a= scipy.stats.entropy(values,base=2)
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT
    if(a==0.0):
        CONSTANT_COUNT += 1
    elif(a<round(math.log2(N/2),2)):
        RANDOM_COUNT +=1
    elif(a==round(math.log2(N/2),2)):
            RANDOM_COUNT +=1
            GLOBAL_COUNT +=1
            LOCAL_COUNT  +=1
    else:
        ODD_COUNT +=1

def entropy_s(values, N):
    a= scipy.stats.entropy(values,base=2)
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT

    if(a==0.0):
        CONSTANT_COUNT += 1
    elif(a<round(math.log2(N),2)):
        LOCAL_COUNT +=1
        RANDOM_COUNT +=1
    elif(a==round(math.log2(N),2)):
            RANDOM_COUNT +=1
            GLOBAL_COUNT += 1
            LOCAL_COUNT += 1
    else:
        ODD_COUNT +=1

def entropy_xprime(values, N):
    b = np.array(a_derivative(values))
    d = abs(b)
    a= scipy.stats.entropy(d,base=2)
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT

    if(a==0.0):
        CONSTANT_COUNT += 1
        LOCAL_COUNT += 1
        GLOBAL_COUNT += 1
    elif(a<=round(math.log2(N/2),2)):
        RANDOM_COUNT +=1
    else:
        ODD_COUNT +=1

def entropy_sprime(values, N):
    b = np.array(a_derivative(values))
    d = abs(b)
    a = scipy.stats.entropy(d,base=2)
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT

    if(a==0.0):
        CONSTANT_COUNT += 1
        GLOBAL_COUNT += 1
    elif(a==1.0):
        LOCAL_COUNT += 1
    elif(a<=round(math.log2(N),2)):
        RANDOM_COUNT +=1
    else:
        ODD_COUNT +=1

def standard_deviation_x(values, N):
    a =(np.std(values))
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT

    if(a==0.0):
        CONSTANT_COUNT += 1
    elif(a==round(math.sqrt((math.pow(N,2)-4))/48), 2):
        LOCAL_COUNT += 1
    elif(a==round(math.sqrt((math.pow(N,2)-4))/12), 2):
        GLOBAL_COUNT += 1
    elif(a==round((math.pow(2,16)-1)/math.sqrt(12)), 2):
        RANDOM_COUNT +=1
    else:
        ODD_COUNT +=1

def standard_deviation_s(values, N):
    a =(np.std(values))
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT

    if(a==0.0):
        CONSTANT_COUNT += 1
    elif(a<=round((math.pow(2,16)-1)/math.sqrt(12)), 2):
        LOCAL_COUNT += 1
    elif(a==round(math.sqrt((math.pow(N,2)-1))/12), 2):
        GLOBAL_COUNT += 1
    elif(a==round((math.pow(2,16)-1)/2), 2):
        RANDOM_COUNT +=1
    else:
        ODD_COUNT +=1

def standard_deviation_xprime(values, N):
    b = [a_derivative(values)]
    a =(np.std(b))
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT

    if(a==0.0):
        CONSTANT_COUNT += 1
        GLOBAL_COUNT += 1
        LOCAL_COUNT +=1
    elif(a==round((math.pow(2,16)-1)/math.sqrt(12)), 2):
        RANDOM_COUNT +=1
    else:
        ODD_COUNT +=1


def decision():
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT
    a = {'Constant':CONSTANT_COUNT, 'Local':LOCAL_COUNT, 'Global': GLOBAL_COUNT, 'Random':RANDOM_COUNT,'Odd': ODD_COUNT}
    b = max(a, key=a.get)
    print(b,"is the final decision")
    '''if(CONSTANT_COUNT>RANDOM_COUNT and CONSTANT_COUNT>LOCAL_COUNT and CONSTANT_COUNT>GLOBAL_COUNT and CONSTANT_COUNT>ODD_COUNT ):
        print("It is Constant")
    elif(LOCAL_COUNT>RANDOM_COUNT and LOCAL_COUNT>CONSTANT_COUNT and LOCAL_COUNT>GLOBAL_COUNT and LOCAL_COUNT>ODD_COUNT):
        print("It is Local")
    elif(GLOBAL_COUNT>RANDOM_COUNT and GLOBAL_COUNT>LOCAL_COUNT and GLOBAL_COUNT>ODD_COUNT and GLOBAL_COUNT>CONSTANT_COUNT):
        print("It is GLobal")
    elif(RANDOM_COUNT>CONSTANT_COUNT and RANDOM_COUNT>LOCAL_COUNT and RANDOM_COUNT>GLOBAL_COUNT and RANDOM_COUNT>ODD_COUNT):
        print("It is Random")
    elif(ODD_COUNT>RANDOM_COUNT and ODD_COUNT>LOCAL_COUNT and ODD_COUNT>GLOBAL_COUNT and ODD_COUNT>CONSTANT_COUNT):
        print("It is Odd")
    else:
        pass'''

# both scores are same
# absolute value look
# ipv6 hitlist and ipv6 ip id capture
def a_derivative (L):
    a = [y - x for x,y in zip(L,L[1:])]
    print([y - x for x,y in zip(L,L[1:])])
    return a


def main():
    a = [41437,40108,41438,40109,41439,40110,41440,40111,41441,40112,41442,40113,41443,40114,41444,40115,40116,41445,40117,41446,40118,40119,41447,40120,41448,40121,40122,41449,40123,41450,40124,40125,41451,40126,41452,40127,41453,40128,41454,40129,41455,40130,40131,41456,40132,41457,40133,41458,40134,41459,40135,41460,40136,41461,40137,41462,40138,41463,40139,41464,40140,41465,40141,41466,40142,41467,40143,41468,40144,41469,40145,41470,40146,41471,40147,41472,40148,41473,40149,41474,40150,41475,40151,41476,40152,41477,40153,40154,41478,40155,41479,40156,40157]
    b = [41437,40108,41438,40109,41439,40110,41440,40111,41441,40112,41442,40113,41443,40114,41444,40115,40116,41445,40117,41446,40118,40119,41447,40120,41448,40121,40122,41449,40123,41450,40124,40125,41451,40126,41452,40127,41453,40128,41454,40129,41455,40130,40131,41456,40132,41457,40133,41458,40134]
    entropy_s(a, 100)
    entropy_x(b,50)
    entropy_sprime(a,100)
    entropy_xprime(b, 50)
    standard_deviation_s(a, 100)
    standard_deviation_x(b, 50)
    #standard_deviation_xprime(b, 50)
    decision()
main()
