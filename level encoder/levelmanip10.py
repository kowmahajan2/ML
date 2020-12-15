import copy
import numpy as np
import pandas as pd
import csv


class Item:
    properties = []

    def __init__(self, proplist):
        self.properties = proplist

    def developProps(self):
        self.index = int(self.properties[0][1])

        self.voxelPos = []
        cut = self.properties[3][1].find(" ")
        i = 0
        self.voxelPos.append(int(self.properties[3][1][i:cut]))
        i = cut
        cut = self.properties[3][1].find(" ", cut + 1)
        self.voxelPos.append(int(self.properties[3][1][i:cut]))
        self.voxelPos.append(int(self.properties[3][1][cut+1:]))

        self.angles = []
        cut = self.properties[5][1].find(" ")
        i = 0
        self.angles.append(int(self.properties[5][1][i:cut]))
        i = cut
        cut = self.properties[5][1].find(" ", cut + 1)
        self.angles.append(int(self.properties[5][1][i:cut]))
        self.angles.append(int(self.properties[5][1][cut+1:]))
                
    
    def printprops(self):
        print(self.properties)
        print(self.voxelPos)
        print(self.angles)

class Connection:

    def __init__(self, proplist):
        self.properties = proplist
    
    def printprops(self):
        print(self.properties)

class Voxel:
    def __init__(self, solid, portal0, portal1, portal2):
        self.solid = solid
        self.portal0 = portal0
        self.portal1 = portal1
        self.portal2 = portal2
        self.itemList = []
        self.oneHotItem = []
    
    def setSolid(self, solid):
        self.solid = solid
    
    def setPortal0(self, portal0):
        self.portal0 = portal0

    def setPortal1(self, portal1):
        self.portal1 = portal1

    def setPortal2(self, portal2):
        self.portal2 = portal2
    
    def addItem(self,newItem):
        self.itemList.append(newItem)

    def printVoxel(self):
        print(self.solid)
    
    def enterVoxel(self):
        ret = [self.solid, self.portal0, self.portal1, self.portal2] + self.oneHotItem
        return ret
    
    def makeOneHot(self):
        self.oneHotItem = [1,0,0,0,0,0]
        for i in self.itemList:
            if(i.properties[1][1] == "ITEM_ENTRY_DOOR"):
                self.oneHotItem = [0,1,0,0,0,0]
            elif(i.properties[1][1] == "ITEM_EXIT_DOOR"):
                self.oneHotItem = [0,0,1,0,0,0]
            elif(i.properties[1][1] == "ITEM_CUBE"):
                self.oneHotItem = [0,0,0,1,0,0]
            elif(i.properties[1][1] == "ITEM_DROPPER_CUBE"):
                self.oneHotItem = [0,0,0,0,1,0]
            elif(i.properties[1][1] == "ITEM_BUTTON_FLOOR"):
                self.oneHotItem = [0,0,0,0,0,1]
    
                

    


class Level:
    def __init__(self):
        self.voxelArray = []
        self.size = []
        self.itemArray = []
        self.connectionArray =[]
        self.limits = 10
    
    def printLevel(self):
        for i in range(0,15):  
            for j in range(0,15):
                for k in range(0,15):
                    Z.voxelArray[i][j][k].printVoxel()

    def LevelRead(self,name):
        level = open(name, 'r+b')
        x = 0
        y = 0
        z = 0


        for line in level:
            if(str(line).find("ChamberSize") != -1):
                tempLine = line
                letter = tempLine[17:18]
                i = 17
                while(letter != b" "):
                    x = x*10 + int(letter.decode("utf-8"))
                    i = i + 1
                    letter = tempLine[i:i+1]
                i = i + 1
                letter = tempLine[i:i+1]
                while(letter != b" "):
                    y = y*10 + int(letter.decode("utf-8"))
                    i = i + 1
                    letter = tempLine[i:i+1]
                i = i + 1
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    z = z*10 + int(letter.decode("utf-8"))
                    i = i + 1
                    letter = tempLine[i:i+1]
                break

        #print(x)
        #print(y)
        #print(z)
        self.size = [x,y,z]
        X = []
        Y = []
        Z = []
        for i in range(0,self.limits):
            for j in range(0,self.limits):
                for k in range(0,self.limits):
                    X.append(Voxel(1,1,1,1))
                Y.append(X)
                X = []
            Z.append(Y)
            Y = []
        
        #print(np.shape(Z))
        
        """for line in level:
            
            if((str(line).find("Solid") != -1)):
                for line in level:
                    tempLine = line
                    print(tempLine)
                    if(str(tempLine).find("f") != -1):
                        i = 12
                        #print(i)
                        letter = tempLine[i:i+1]
                        while(letter != b'"'):
                            print(letter)
                            X.append(Voxel(int(letter.decode("utf-8")),1,1,1))
                            i = i + 1
                            letter = tempLine[i:i+1]
                        #print("Length of X" + str(len(X)))
                        Y.append(X)
                        X = []
                    elif(str(tempLine).find("}") != -1):
                        #print("Length of Y" + str(len(Y)))
                        Z.append(Y)
                        Y = []
                    elif(str(tempLine).find("Portal0") != -1):
                        #print(len(Z))
                        break"""
                
        xIter = 0
        yIter = 0
        zIter = 0
        #solid
        for line in level:
            tempLine = line
            #print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    #print(letter)
                    Z[zIter][yIter][xIter].setSolid(int(letter.decode("utf-8")))
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
            elif(str(tempLine).find("Portal0") != -1):
                #print(len(Z))
                break

        xIter = 0
        yIter = 0
        zIter = 0
        #portal0
        for line in level:
            tempLine = line
            #print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    #print(letter)
                    Z[zIter][yIter][xIter].setPortal0(int(letter.decode("utf-8")))
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
                #print(len(Z))
                break
        
        xIter = 0
        yIter = 0
        zIter = 0
        #portal1
        for line in level:
            tempLine = line
            #print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    #print(letter)
                    Z[zIter][yIter][xIter].setPortal1(int(letter.decode("utf-8")))
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
                #print(len(Z))
                break

        xIter = 0
        yIter = 0
        zIter = 0
        #portal2
        for line in level:
            tempLine = line
            #print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    #print(letter)
                    Z[zIter][yIter][xIter].setPortal2(int(letter.decode("utf-8")))
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
                #print(len(Z))
                break
        
        #print(line)
        self.voxelArray = copy.deepcopy(Z)

        itemList = []
        connectionList = []

        itemPropList = []
        prop = ""
        value = ""
        propTupple = []

                #iterating over all the lines
        
        for line in level:
            #print(line)
            #print("hey")
            #clearing property and value strings at the start of each line
            prop = ""
            value = ""

            #check if the string contains "Item" and not "Items"
            if((str(line).find("Item") != -1) and (str(line).find("Items") == -1)):
                
                itemPropList = []
                for line in level:
                    tempLine = line
                    prop = ""
                    value = ""
                    propTupple = []
                    i = 0
                    #if line contains "{" do nothing
                    if(str(tempLine).find("{")!= -1):
                        pass
                        #print("do nothing")
                    elif(str(tempLine).find("}")!= -1):
                        if(len(itemPropList) > 0):
                            newItem = Item(itemPropList)
                            newItem.developProps()
                            """print(len(self.voxelArray))
                            print(len(self.voxelArray[0]))
                            print(len(self.voxelArray[0][0]))
                            print(len(newItem.voxelPos))"""
                            #print(newItem.voxelPos)
                            self.voxelArray[newItem.voxelPos[2]][newItem.voxelPos[1]][newItem.voxelPos[0]].itemList.append(newItem)
                            itemList.append(newItem)
                            itemPropList = []
                            break
                    else:

                        #skipping the 3 tabs and the inverted comma
                        letter = tempLine[4:5]
                        i = 4
                        #recording the string uptill the next inverted comma
                        while(letter != b'"'):
                            prop = "".join([prop, letter.decode("utf-8")])
                            i = i + 1
                            letter = tempLine[i:i+1]
                        
                        #skipping the 2 tabs uptill the next inverted comma
                        i = i + 4
                        letter = tempLine[i:i+1]

                        #recording the string uptill the next inverted comma
                        while(letter != b'"'):
                            
                            value = "".join([value, letter.decode("utf-8")])
                            i = i+1
                            letter = tempLine[i:i+1]
                        
                        

                        
                        #print(prop)
                        #print(value)
                        propTupple.append(prop)
                        propTupple.append(value)
                
                #adding property to the current list
                        itemPropList.append(propTupple)

                self.itemArray = copy.deepcopy(itemList)

                        

                #restting the property tupple
            if((str(line).find("Connection") != -1) and (str(line).find("Connections") == -1)):
                
                connectionPropList = []
                for line in level:
                    tempLine = line
                    prop = ""
                    value = ""
                    propTupple = []
                    i = 0
                    #if line contains "{" do nothing
                    if(str(tempLine).find("{")!= -1):
                        pass
                        #print("do nothing")
                    elif(str(tempLine).find("}")!= -1):
                        if(len(connectionPropList) > 0):
                            newConnection = Connection(connectionPropList)
                            connectionList.append(newConnection)
                            connectionPropList = []
                            break
                    else:

                        #skipping the 3 tabs and the inverted comma
                        letter = tempLine[4:5]
                        i = 4
                        #recording the string uptill the next inverted comma
                        while(letter != b'"'):
                            prop = "".join([prop, letter.decode("utf-8")])
                            i = i + 1
                            letter = tempLine[i:i+1]
                        
                        #skipping the 2 tabs uptill the next inverted comma
                        i = i + 4
                        letter = tempLine[i:i+1]

                        #recording the string uptill the next inverted comma
                        while(letter != b'"'):
                            
                            value = "".join([value, letter.decode("utf-8")])
                            i = i+1
                            letter = tempLine[i:i+1]
                        
                        

                        
                        #print(prop)
                        #print(value)
                        propTupple.append(prop)
                        propTupple.append(value)
                
                #adding property to the current list
                        connectionPropList.append(propTupple)
                self.connectionArray = copy.deepcopy(connectionList)

        #print(len(itemList))
        #print(len(connectionList))
        #itemList[2].printprops()
    
        
    def developOneHot(self):
        for i in range(0,16):
            for j in range(0,16):
                for k in range(0,16):
                    self.voxelArray[i][j][k].makeOneHot()

    def makeCSVarray(self):
        Z = []
        Y = []
        X = []
        for i in range(0,16):
            for j in range(0,16):
                for k in range(0,16):
                    X.append(self.voxelArray[i][j][k].enterVoxel())
                Y.append(X)
                X = []
            Z.append(Y)
            Y = []
        return Z
    
        

data = []

for k in range(0,26):
    print(k)
    name = "level (" +str(k + 1) + ").p2c"
    newLevel = Level()
    newLevel.LevelRead(name)
    newLevel.developOneHot()
    Z = newLevel.makeCSVarray()
    data.append(Z)
    data.append(np.rot90(Z,1,(1,2)))
    data.append(np.rot90(Z,2,(1,2)))
    data.append(np.rot90(Z,3,(1,2)))
    data.append(np.flip(Z,1))
    data.append(np.rot90(np.flip(Z,1),1,(1,2)))
    data.append(np.rot90(np.flip(Z,1),2,(1,2)))
    data.append(np.rot90(np.flip(Z,1),3,(1,2)))
    del newLevel

print(np.shape(data))


df = pd.DataFrame(data)

df.to_csv('Data.csv',header = False, index = False)





                


