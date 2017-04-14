import processing.inputOperators as inputOperators
import processing.GearBuilder as GearBuilder

headList = ["head"]
armsList = ["arms"]
chestList = ["chest"]
legsList = ["legs"]
classItemList = ["classItem"]
ghostList = ["ghost"]
artifactList = ["artifact"]
    
allGear = [headList, armsList, chestList, legsList, classItemList, ghostList,    artifactList]
    
def createBuilds():
    temp = [[],[],[],[],[],[],[]]
    
    buildList = []
    
    for i in range(len(allGear)):
        for k in range(len(allGear[i])-1):
            for j in range(2):
                
                allGear[i][k+1].setSelector(j+1)
                
                if allGear[i][k+1].getSpread() == GearBuilder.statSpread[0]:
                    one = allGear[i][k+1].getInt()
                    two = allGear[i][k+1].getDis()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[1]:
                    one = allGear[i][k+1].getInt()
                    two = allGear[i][k+1].getStr()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[2]:
                    one = allGear[i][k+1].getDis()
                    two = allGear[i][k+1].getStr()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[3]:
                    one = allGear[i][k+1].getInt()
                    two = allGear[i][k+1].getDis()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[4]:
                    one = allGear[i][k+1].getInt()
                    two = allGear[i][k+1].getStr()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[5]:
                    one = allGear[i][k+1].getDis()
                    two = allGear[i][k+1].getInt()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[6]:
                    one = allGear[i][k+1].getDis()
                    two = allGear[i][k+1].getStr()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[7]:
                    one = allGear[i][k+1].getStr()
                    two = allGear[i][k+1].getInt()
                elif allGear[i][k+1].getSpread() == GearBuilder.statSpread[8]:
                    one = allGear[i][k+1].getStr()
                    two = allGear[i][k+1].getDis()
                
                allGear[i][k+1].setStats(one, two, allGear[i][k+1].getSpread())
                
                temp[i].append([allGear[i][k+1].getInt(), allGear[i][k+1].getDis(), allGear[i][k+1].getStr()])

    
    for a in range(len(temp[0])):
        for b in range(len(temp[1])):
            for c in range(len(temp[2])):
                for d in range(len(temp[3])):
                    for e in range(len(temp[4])):
                        for f in range(len(temp[5])):
                            for g in range(len(temp[6])):
                                
                                new = [temp[0][a], temp[1][b], temp[2][c], temp[3][d], temp[4][e], temp[5][f], temp[6][g]]
                                
                                if new not in buildList:
                                    buildList.append(new)
    
    return buildList
