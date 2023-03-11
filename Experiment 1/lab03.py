#-----------------lab no 3---------------------------------------
#-------------------experiment no 1------------------------------
import csv
numm=3
a=[]
print("\n The given training data set \n")
with open("D:/MIET/AI with computer Vision/2020a1r003_dataset.csv",'r') as csvfile:
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
    if a[i][numm]=="positive":
        for j in range(0,numm):
            if a[i][j]!= hypothesis[j]:
                hypothesis[j]='?'
            else:
                hypothesis[j]=a[i][j]
    print("For training instance no:{0} the hypothesis is".format(i),hypothesis)
print("\n The maximally specific hypothesis for a given training example: \n")
print(hypothesis)


#------------experiment no2-------------------
#for a given set of training data examples stored in the .csv files,implement and demonstrate the Data Visualization
#to output a description of the set of all hypothesis consistent with the training examples. 
#--------candidate elimination algorithm-----------------------
'''
Like find S but it take both +ve and -ve training samples
specific and generic hypothesis.


'''