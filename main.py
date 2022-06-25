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
    if(math.isnan(a) == True):
        a = 0.0
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
    if(math.isnan(a) == True):
        a = 0.0
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
    if(math.isnan(a) == True):
        a = 0.0
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
    if(math.isnan(a) == True):
        a = 0.0
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
    if(math.isnan(a) == True):
        a = 0.0
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
    if(math.isnan(a) == True):
        a = 0.0
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
    b = np.array(a_derivative(values))
    d = abs(b)
    a =(np.std(d))
    global CONSTANT_COUNT,RANDOM_COUNT,LOCAL_COUNT,GLOBAL_COUNT,ODD_COUNT
    if(math.isnan(a) == True):
        a = 0.0
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

    data = {'Constant':CONSTANT_COUNT, 'Local':LOCAL_COUNT, 'Global': GLOBAL_COUNT, 'Random':RANDOM_COUNT,'Odd': ODD_COUNT}

    # Here, we create a dict of lists, where the keys are the scores, and the values
    # are the names of each person who has that score.  This will produce:
    #
    # {
    #     35.0: ['Diane'],
    #     95.0: ['Bion', 'Sam'],
    #     125.0: ['Jack']
    #  }

    collected = {}

    # For each key (name) in the input dict...
    for name in data:
        # Get the score value out of the array for this name
        val = data[name]

        # If we don't have an entry in our new dict for this score (no key in the dict of that
        # score value) then add that entry as the score for the key and an empty array for the value
        if val not in collected:
            collected[val] = []

        # Now that we're sure we have an entry for the score of the name we're processing, add
        # the name to the array for that score in the new dict
        collected[val].append(name)

    # Now we just "flip" each entry in the 'collected' map to create a new dict.  We create
    # one entry in this dict for each entry in the 'collected' map, where each key is a
    # single string where we've combined all of the names with the same score, separated
    # by 'and', and each value is the score that those names had.

    result = {}

    # Now iterate over each of our keys, the unique scores, in our new 'collected' dict...
    for val in collected:

        # We only want to create an entry in the new dict if the entry we're processing has more than
        # just one name in the list of names.  So here, we check for that, and skip adding an entry to
        # the new dict if there is only one name in the list
        if len(collected[val]) == 1:
            continue

        # Combine the value of this entry, the list of names with a particular score, into a single string
        combinedNames = " and ".join(collected[val])

        # Add an entry to our 'result' dict with this combined name as the key and the score as the value
        result[combinedNames] = val

    # Print each combined name string from the resulting structure
    for names in result:
        print(names)
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
    return a


def main():
    a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    entropy_s(a, 100)
    entropy_x(b,50)
    entropy_sprime(a,100)
    entropy_xprime(b, 50)
    standard_deviation_s(a, 100)
    standard_deviation_x(b, 50)
    standard_deviation_xprime(b, 50)
    decision()
main()
