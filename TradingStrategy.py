import types

class TradingStrategy:
   name = ""
   stateMachine = None

   def __init__(self, stateMachine = None):
      self.stateMachine = stateMachine

   def onEnter(self): pass
   def onExecute(self): pass
   def onExit(self): pass

###
#  NONE
###
class TradingStrategyNone(TradingStrategy):
   name = "None"

   def onEnter(self):
      print("Enter  :", self.name)
   
   def onExecute(self):
      print("Execute:", self.name)
   
   def onExit(self):
      print("Exit   :", self.name)

