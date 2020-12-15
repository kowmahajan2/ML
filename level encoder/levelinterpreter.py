import copy
import numpy as np
import pandas as pd
import csv

dataN = pd.read_csv('finalevel11.csv')
dataN = np.array(dataN)
print(dataN)
levelsize = 10
NewZ = np.reshape(dataN,(levelsize,levelsize,levelsize,10))

level = open("1607539864.p2c", 'r+b')
newlevel = open("testfile11.p2c", "wb+")
"""X = []
Y = []
Z = []
for i in range(0,16):
    for j in range(0,16):
        for k in range(0,16):
            X.append(Voxel(1,1,1,1))
        Y.append(X)
        X = []
    Z.append(Y)
    Y = []"""

#print(np.shape(Z))
for line in level:
    tempLine = line
    newlevel.write(tempLine)
    if(str(tempLine).find("Voxels") != -1):
        break
      
xIter = 0
yIter = 0
zIter = 0
#solid
for line in level:
    tempLine = line
    print(tempLine)
    if(str(tempLine).find("f") != -1):
        i = str(tempLine).find("f")-7
        print(i)
        letter = tempLine[i:i+1]
        while(letter != b'"'):
            print(letter)
            if(NewZ[zIter][yIter][xIter][0] == 0):
                tempLine = tempLine[:i] + b"0" + tempLine[i+1:]
            if(NewZ[zIter][yIter][xIter][0] == 1):
                tempLine = tempLine[:i] + b"1" + tempLine[i+1:]
            xIter = xIter + 1
            i = i + 1
            letter = tempLine[i:i+1]
        print("Length of X" + str(xIter))
        yIter = yIter + 1
        xIter = 0
    elif(str(tempLine).find("}") != -1):
        #print("Length of Y" + str(len(Y)))
        zIter = zIter + 1
        yIter = 0
    elif(str(tempLine).find("Portal0") != -1):
        #print(len(Z))
        newlevel.write(tempLine)
        break
    newlevel.write(tempLine)

xIter = 0
yIter = 0
zIter = 0
#portal0
for line in level:
    tempLine = line
    #print(tempLine)
    if(str(tempLine).find("f") != -1):
        i = str(tempLine).find("f") - 7
        #print(i)
        letter = tempLine[i:i+1]
        while(letter != b'"'):
            #print(letter)
            if(NewZ[zIter][yIter][xIter][1] == 0):
                tempLine = tempLine[:i] + b"0" + tempLine[i+1:]
            if(NewZ[zIter][yIter][xIter][1] == 1):
                tempLine = tempLine[:i] + b"1" + tempLine[i+1:]
            xIter = xIter + 1
            i = i + 1
            letter = tempLine[i:i+1]
        #print("Length of X" + str(len(X)))
        yIter = yIter + 1
        xIter = 0
    elif(str(tempLine).find("}") != -1):
        #print("Length of Y" + str(len(Y)))
        zIter = zIter + 1
        yIter = 0
    elif(str(tempLine).find("Portal1") != -1):
        newlevel.write(tempLine)
        #print(len(Z))
        break
    newlevel.write(tempLine)

xIter = 0
yIter = 0
zIter = 0
#portal1
for line in level:
    tempLine = line
    #print(tempLine)
    if(str(tempLine).find("f") != -1):
        i = str(tempLine).find("f") - 7
        #print(i)
        letter = tempLine[i:i+1]
        while(letter != b'"'):
            #print(letter)
            if(NewZ[zIter][yIter][xIter][2] == 0):
                tempLine = tempLine[:i] + b"0" + tempLine[i+1:]
            if(NewZ[zIter][yIter][xIter][2] == 1):
                tempLine = tempLine[:i] + b"1" + tempLine[i+1:]
            xIter = xIter + 1
            i = i + 1
            letter = tempLine[i:i+1]
        #print("Length of X" + str(len(X)))
        yIter = yIter + 1
        xIter = 0
    elif(str(tempLine).find("}") != -1):
        #print("Length of Y" + str(len(Y)))
        zIter = zIter + 1
        yIter = 0
    elif(str(tempLine).find("Portal2") != -1):
        newlevel.write(tempLine)
        #print(len(Z))
        break
    newlevel.write(tempLine)

xIter = 0
yIter = 0
zIter = 0
#portal2
for line in level:
    tempLine = line
    #print(tempLine)
    if(str(tempLine).find("f") != -1):
        i = str(tempLine).find("f") - 7
        #print(i)
        letter = tempLine[i:i+1]
        while(letter != b'"'):
            #print(letter)
            if(NewZ[zIter][yIter][xIter][3] == 0):
                tempLine = tempLine[:i] + b"0" + tempLine[i+1:]
            if(NewZ[zIter][yIter][xIter][3] == 1):
                tempLine = tempLine[:i] + b"1" + tempLine[i+1:]
            xIter = xIter + 1
            i = i + 1
            letter = tempLine[i:i+1]
        #print("Length of X" + str(len(X)))
        yIter = yIter + 1
        xIter = 0
    elif(str(tempLine).find("}") != -1):
        #print("Length of Y" + str(len(Y)))
        zIter = zIter + 1
        yIter = 0
    elif(str(tempLine).find("Items") != -1):
        pass
    newlevel.write(tempLine)

#print(line)
#self.voxelArray = copy.deepcopy(Z)