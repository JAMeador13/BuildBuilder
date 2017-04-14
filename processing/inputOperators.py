import processing.GearBuilder as GearBuilder

def selectType(typeSelection, spreadSelection):
    if typeSelection == 1:
        head = GearBuilder.Head(0, 0, 0, spreadSelection)
        return head
    elif typeSelection == 2:
        arms = GearBuilder.Arms(0, 0, 0, spreadSelection)
        return arms
    elif typeSelection == 3:
        chest = GearBuilder.Chest(0, 0, 0, spreadSelection)
        return chest
    elif typeSelection == 4:
        legs = GearBuilder.Legs(0, 0, 0, spreadSelection)
        return legs
    elif typeSelection == 5:
        classItem = GearBuilder.ClassItem(0, 0, 0, spreadSelection)
        return classItem
    elif typeSelection == 6:
        ghost = GearBuilder.Ghost(0, 0, 0, spreadSelection)
        return ghost
    elif typeSelection == 7:
        artifact = GearBuilder.Artifact(0, 0, 0, spreadSelection)
        return artifact

def selectSpread(spreadSelection):
    
    if spreadSelection == GearBuilder.statSpread[0]:
                
        first = int(input("Enter intellect value (without node selected): "))
        second = int(input("Enter discipline value (without node selected): "))
        
    elif spreadSelection == GearBuilder.statSpread[1]:
                
        first = int(input("Enter intellect value (without node selected): "))
        second = int(input("Enter strength value (without node selected): "))
                
    elif spreadSelection == GearBuilder.statSpread[2]:
                
        first = int(input("Enter discipline value (without node selected): "))
        second = int(input("Enter strength value (without node selected): "))
                
    elif spreadSelection == GearBuilder.statSpread[3] or spreadSelection == GearBuilder.statSpread[4]:
                
        first = int(input("Enter intellect value (without node selected): "))
        second = 0
                
    elif spreadSelection == GearBuilder.statSpread[5] or spreadSelection == GearBuilder.statSpread[6]:
                
        first = int(input("Enter discipline value (without node selected): "))
        second = 0
                
    elif spreadSelection == GearBuilder.statSpread[7] or spreadSelection == GearBuilder.statSpread[8]:
                
        second = 0
        first = int(input("Enter strength value (without node selected): "))

    return first, second
