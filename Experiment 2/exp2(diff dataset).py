#------------------experiment no:2-------------------------------------
'''candidate elimination algorithm:- set of all hypothesis:- set of general(G) and specific hypothesis(S)
G noted by null.
1)initialize the version space V to contain all possible hypothesis in hypo space H.
2)for each training example:
    if example is positive,remove from V all hypothesis that are inconistent with the example.
    a hypothesis is inconsistent if any of its attribute values differ from the example.
    a hypothesis is negative,remove from v all hypothesis that are consistent with the example.
    a hypothesis is consistent if all of its attribute value match the example.
    if there are any remaining hypothesis in V after step 2, generalize and/or specialize them as needed to include the current example.
#-------------------------------------------------------------------------------------------------------------------------------'''
import numpy as np
import pandas as pd

data=pd.DataFrame(data=pd.read_csv("C:/Users/Aditya Raina/OneDrive/Desktop/testing datatset.csv"))
print(data)
concepts=np.array(data.iloc[:,0:-1])
print(concepts)

target=np.array(data.iloc[:,-1])
print(target)

def learn(concepts,target):
    specific_h=concepts[0].copy()
    print("\n Initializiation of specific h and general h")
    print(specific_h)

    general_h=[["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print(general_h)

    for i,h in enumerate(concepts):
        if target[i]=="yes":
            for x in range(len(specific_h)):

                if h[x]!=specific_h[x]:
                    specific_h[x]="?"
                    general_h[x][x]="?"

        if target[i]=="no":
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    general_h[x][x]==specific_h[x]
                else:
                    general_h[x][x]=="?"
        print("\n Steps of Candidate elimination Algorithm",i+1)
        print(specific_h)
        print(general_h)

    indices=[i for i,val in enumerate(general_h) if val==['?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?'])
    return specific_h,general_h
s_final, g_final=learn(concepts,target)
print("\nFinal specific_h:",s_final,sep="\n")
print("\nFinal general_h:",g_final,sep="\n")

