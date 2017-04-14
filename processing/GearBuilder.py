statSpread = ["ID", "IS", "DS", "Id", "Is", "Di", "Ds", "Si", "Sd", "special"]
titles = ["head", "arms", "chest", "legs", "classItem", "ghost", "artifact"]

class Gear(object):
  def __init__(self):
    self.title = ""
    self.int = 0
    self.dis = 0
    self.str = 0
    self.maxStat = 0
    self.selector = 0
    self.interval = 0
    self.spread = ""
    
  def setStats(self, first, second, spread):
    
    self.spread = spread
    
    if first > self.maxStat:
        lowerFirst = True
        lowerSecond = False
    elif second > self.maxStat:
        lowerFirst = False
        lowerSecond = True
    else:
        lowerFirst = False
        lowerSecond = False
    
    if lowerFirst:
        if self.selector == 0:
          first = first - self.interval
          second = second
        elif self.selector == 1:
          first = first
          second = second
        elif self.selector == 2:
          first = first - self.interval
          second = second + self.interval
          
    elif lowerSecond:
        if self.selector == 0:
          first = first
          second = second - self.interval
        elif self.selector == 1:
          first = first + self.interval
          second = second - self.interval
        elif self.selector == 2:
          first = first
          second = second
          
    else:
        if self.selector == 0:
          first = first
          second = second
        elif self.selector == 1:
          first = first + self.interval
          second = second
        elif self.selector == 2:
          first = first
          second = second + self.interval
    
    if spread == statSpread[0]:
      self.int = first
      self.dis = second
    elif spread == statSpread[1]:
      self.int = first
      self.str = second
    elif spread == statSpread[2]:
      self.dis = first
      self.str = second
    elif spread == statSpread[3]:
      self.int = first
      self.dis = second
    elif spread == statSpread[4]:
      self.int = first
      self.str = second
    elif spread == statSpread[5]:
      self.dis = first
      self.int = second
    elif spread == statSpread[6]:
      self.dis = first
      self.str = second
    elif spread == statSpread[7]:
      self.str = first
      self.int = second
    elif spread == statSpread[8]:
      self.str = first
      self.dis = second

  def setSpread(self, spread):
      self.spread = spread
    
  def setSelector(self, x):
      self.selector = x

  def setMax(self, x):
      self.maxStat = x
    
  def setInterval(self, x):
      self.interval = x

  def setTitle(self, x):
      self.title = x
    
  def getInt(self):
    return self.int
  
  def getDis(self):
    return self.dis
  
  def getStr(self):
    return self.str
    
  def getSpread(self):
    return self.spread

  def getStats(self):
    return self.spread, self.int, self.dis, self.str
    
  
class Head(Gear):  #1st stat num, 2nd stat num, int 0-2, string from statSpread
  def __init__(self, first, second, selector, spread):
    super().__init__()
    super().setTitle(titles[0])
    super().setMax(46)
    super().setInterval(19)
    super().setSelector(selector)
    super().setStats(first, second, spread)

class Arms(Gear):
  def __init__(self, first, second, selector, spread):
    super().__init__()
    super().setTitle(titles[1])
    super().setMax(41)
    super().setInterval(17)
    super().setSelector(selector)
    super().setStats(first, second, spread)

class Chest(Gear):
  def __init__(self, first, second, selector, spread):
    super().__init__()
    super().setTitle(titles[2])
    super().setMax(61)
    super().setInterval(25)
    super().setSelector(selector)
    super().setStats(first, second, spread)

class Legs(Gear):
  def __init__(self, first, second, selector, spread):
    super().__init__()
    super().setTitle(titles[3])
    super().setMax(56)
    super().setInterval(23)
    super().setSelector(selector)
    super().setStats(first, second, spread)

class ClassItem(Gear):
  def __init__(self, first, second, selector, spread):
    super().__init__()
    super().setTitle(titles[4])
    super().setMax(25)
    super().setInterval(10)
    super().setSelector(selector)
    super().setStats(first, second, spread)
  
class Ghost(Gear):
  def __init__(self, first, second, selector, spread):
    super().__init__()
    super().setTitle(titles[5])
    super().setMax(25)
    super().setInterval(10)
    super().setSelector(selector)
    super().setStats(first, second, spread)

class Artifact(Gear):
  def __init__(self, first, second, selector, spread):
    super().__init__()
    super().setTitle(titles[6])
    super().setMax(38)
    self.disMax = 51
    super().setInterval(43)
    super().setSelector(selector)
    super().setStats(first, second, spread)
