#----------------------------------------------
'''import matplotlib.pyplot as plt
listt=[1,2,3,4,45]
listt1=[2,3,4,6,7]
plt.plot(listt,listt1)
plt.show()  # to show the graph'''
#------------experiment no:-1-------------------
'''
algorithm to find maximally specific hypothesis given a  set of trainig examples.
FIND S-algorithm-->positive(1),-->negative(0)[ignored]
1.initialize the hypothesis set to the general hypothesis.
2.in each training example:
    a)if example is positive, remove from the hypothesis set an hypothesis that is not consistent with the example.
    b)if negative,dont update the hypothesis list.
3).return the maximally specific hypothesis.

'''
#----------------experiment no 1------------------------------
import csv
numm=6
a=[]
print("\n The given training data set \n")
with open("C:/Users/Aditya Raina/Downloads/test.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)
print("\n The initial values of hypothesis \n")
hypothesis=['0']*numm
print(hypothesis)

for j in range(0,numm):
    hypothesis[j]= a[0][j]
print("\n Find S: Finding a maximally specific hypothesis \n")
for i in range(0,len(a)):
    if a[i][numm]=="Yes":
        for j in range(0,numm):
            if a[i][j]!= hypothesis[j]:
                hypothesis[j]='?'
            else:
                hypothesis[j]=a[i][j]
    print("For training instance no:{0} the hypothesis is".format(i),hypothesis)
print("\n The maximally specific hypothesis for a given training example: \n")
print(hypothesis)
