import processing.GearBuilder as GearBuilder
import re

class Build:
  def __init__(self):
    self.head = [0, 0, 0]
    self.arms = [0, 0, 0]
    self.chest = [0, 0, 0]
    self.legs = [0, 0, 0]
    self.classItem = [0, 0, 0]
    self.ghost = [0, 0, 0]
    self.artifact = [0, 0, 0]
    
    self.intellect = 0
    self.discipline = 0
    self.strength = 0
    
    self.intTier = 0
    self.disTier = 0
    self.strTier = 0
    self.totTier = 0


# gearList takes a list of 7 lists
  def createBuild(self, gearList): 
    self.head = gearList[0]
    self.arms = gearList[1]
    self.chest = gearList[2]
    self.legs = gearList[3]
    self.classItem = gearList[4]
    self.ghost = gearList[5]
    self.artifact = gearList[6]
    
    self.intellect = sum([self.head[0], self.arms[0], self.chest[0], self.legs[0], self.classItem[0], self.ghost[0], self.artifact[0]])
    
    self.discipline = sum([self.head[1], self.arms[1], self.chest[1], self.legs[1], self.classItem[1], self.ghost[1], self.artifact[1]])
    
    self.strength = sum([self.head[2], self.arms[2], self.chest[2], self.legs[2], self.classItem[2], self.ghost[2], self.artifact[2]])
    
    if self.intellect > 359:
      self.intTier = 5
    else:
      self.intTier = self.intellect // 60
    
    if self.discipline > 359:
      self.disTier = 5
    else:
      self.disTier = self.discipline // 60
    
    if self.strength > 359:
      self.strTier = 5
    else:
      self.strTier = self.strength // 60
      
    self.totTier = self.intTier + self.disTier + self.strTier
  
  def getStats(self):
    return self.head, self.arms, self.chest, self.legs, self.classItem, self.ghost, self.artifact, self.intellect, self.discipline, self.strength, self.intTier, self.disTier, self.strTier, self.totTier
  
  def printBuild(self):
    a,b,c,d,e,f,g,h,i,j,k,l,m,n = self.getStats()
    
    tem = "             Int Dis Str" + "\n" + \
          "Head       : "+ str(a[0]).zfill(3)+" "+ str(a[1]).zfill(3)+" "+ str(a[2]).zfill(3) + "\n"\
          "Arms       : "+ str(b[0]).zfill(3)+" "+ str(b[1]).zfill(3)+" "+ str(b[2]).zfill(3) + "\n"\
          "Chest      : "+ str(c[0]).zfill(3)+" "+ str(c[1]).zfill(3)+" "+ str(c[2]).zfill(3) + "\n"\
          "Legs       : "+ str(d[0]).zfill(3)+" "+ str(d[1]).zfill(3)+" "+ str(d[2]).zfill(3) + "\n"\
          "Class Item : "+ str(e[0]).zfill(3)+" "+ str(e[1]).zfill(3)+" "+ str(e[2]).zfill(3) + "\n"\
          "Ghost      : "+ str(f[0]).zfill(3)+" "+ str(f[1]).zfill(3)+" "+ str(f[2]).zfill(3) + "\n"\
          "Artifact   : "+ str(g[0]).zfill(3)+" "+ str(g[1]).zfill(3)+" "+ str(g[2]).zfill(3) + "\n"\
          "Totals     : "+ str(h).zfill(3)+" "+ str(i).zfill(3)+" "+ str(j).zfill(3) + "\n"\
          "Tier       :  "+ str(k)+ "   "+ str(l)+ "   "+ str(m)+ "   "+ str(n)
          
    tem = list(tem)
    tem = ''.join(tem)
    tem = str(tem)
          
    tem = re.sub(r" 000", "  - ", tem)
    tem = re.sub(r" 00", "   ", tem)
    tem = re.sub(r" 0", "  ", tem)
        
    print(tem)
  
  
  def printBuildTier(self):
      print("Tier", str(self.totTier), ":", str(self.intTier)+"-"+str(self.disTier)+"-"+str(self.strTier))
      
  def getTier(self):
      return self.totTier
  
  def getIntTier(self):
      return self.intTier
  
  def getDisTier(self):
      return self.disTier
  
  def getStrTier(self):
      return self.strTier
