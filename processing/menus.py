import processing.inputOperators as inputOperators
import processing.actionSelection as actionSelection
import processing.BuildBuilder as BuildBuilder



def menuOne():
    print("Select gear piece to enter:\n"+
          "1. Head\n"+
          "2. Arms\n"+
          "3. Chest\n"+
          "4. Legs\n"+
          "5. Class Item\n"+
          "6. Ghost\n"+
          "7. Artifact\n"+
          "Enter anything else to exit.\n")
    
    typeSelection = str(input("Enter selection number: "))
    print(" ")
    typeOptions = ['1', '2', '3', '4', '5', '6', '7']
    
    if typeSelection not in typeOptions:
        raise EOFError
    
    return int(typeSelection)
  
  
    
def menuTwo():
    print("Select stat spread for item:\n"+
          "1. Int/Dis\n"+
          "2. Int/Str\n"+
          "3. Dis/Str\n"+
          "4. Int with dis sub\n"+
          "5. Int with str sub\n"+
          "6. Dis with int sub\n"+
          "7. Dis with str sub\n"+
          "8. Str with int sub\n"+
          "9. Str with dis sub\n"+
          "0. Special (i.e. Memory of Felwinter)\n"+
          "Enter anything else to exit.\n")
      
    spreadSelection = str(input("Enter selection number: "))
    print(" ")
    spreadOptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    if spreadSelection not in spreadOptions:
        raise EOFError
    
    return spreadSelection
    
    
    
def createObjects(typeSelection, spreadSelection):
    item = inputOperators.selectType(typeSelection, spreadSelection)
    first, second = inputOperators.selectSpread(spreadSelection)
    item.setStats(first, second, spreadSelection)
    print(" ")
    
    for i in range(len(actionSelection.allGear)):
        if item.title == actionSelection.allGear[i][0]:
            actionSelection.allGear[i].append(item)
    
    for i in range(len(actionSelection.allGear)):
        if len(actionSelection.allGear[i]) > 1:
            buildReady = True
        else:
            buildReady = False
            break
    
    return buildReady



def buildReadyMenu(buildReady):
    
    if buildReady:
        print("Please select next action:\n"+
              "1. Enter another item\n"+
              "2. Calculate best builds with current items\n"+
              "3. Enter build to produce with current items\n"+
              "Enter anything else to exit.\n")
        actionSelect = str(input("Enter selection number: "))
        print(" ")
        actionOptions = ['1', '2', '3']
        
    else:
        print("Please select next action:\n"+
              "1. Enter another item\n"+
              "Enter anything else to exit.\n")
        actionSelect = str(input("Enter selection number: "))
        print(" ")
        actionOptions = ['1']
    
    if actionSelect not in actionOptions:
        raise EOFError
    
    return int(actionSelect)
    
    
    
def actionSelections(actionSelect):
    if actionSelect == 1:
        return True

    elif actionSelect == 2:
        
        builds = actionSelection.createBuilds()
        buildsList = []
        
        for i in range(len(builds)):
            
            newBuild = BuildBuilder.Build()
            newBuild.createBuild(builds[i])
            buildsList.append(newBuild)
            
            if newBuild.getTier() == 12:
                newBuild.printBuild()
    
    elif actionSelect == 3:
        
        while True:
            
            try:
                
                print("To generate builds with current gear, enter the desired tiers as follows:\n"+
                      "INT-DIS-STR\n"+
                      "Example: 5-5-2\n")
                tierSelection = str(input("Tier to produce: "))
                print(" ")
                
                intTier = int(tierSelection[0])
                disTier = int(tierSelection[2])
                strTier = int(tierSelection[4])
            
            except ValueError:
                print("Invalid input. Try again.")
                continue
            
            else:
                break
        
        builds = actionSelection.createBuilds()
        buildsList = []
        
        for i in range(len(builds)):
            
            newBuild = BuildBuilder.Build()
            newBuild.createBuild(builds[i])
            buildsList.append(newBuild)
            
            if [buildsList[i].getIntTier(), buildsList[i].getDisTier(), buildsList[i].getStrTier()] == [intTier, disTier, strTier]:
                buildsList[i].printBuild()
        
        return



def continueCalc():
    quitCalculator = str(input("Are you sure you want to exit? (y/n): "))
    return bool(quitCalculator == "n")
