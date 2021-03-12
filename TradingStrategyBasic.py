import TradingStrategy
import time


def logEvent(self, prefix):
   print(prefix, self.name, "\t", 
      "\tprv:", self.stateMachine.previousState, 
      "\tcur:", self.stateMachine.currentState, 
      "\tnxt:", self.stateMachine.nextState
   )

###
#  IDLE 
###
class Idle(TradingStrategy.TradingStrategy):
   name = "Basic Idle"

   def onEnter(self):
      logEvent(self, "Enter  :")

      self.count = 0
   
   def onExecute(self):
      logEvent(self, "Execute:")

      self.count = self.count + 1
      if self.count < 3: 
         time.sleep(1)
         # Force exit but Keep in the current state ("inTrade") 
         return 
      
      # Change to "onHold" State
      return "onHold"
   
   def onExit(self):
      logEvent(self, "Exit   :")

###
#  ON HOLD
###
class OnHold(TradingStrategy.TradingStrategy):
   name = "Basic OnHold"

   def onEnter(self):
      logEvent(self, "Enter  :")
   
   def onExecute(self):
      logEvent(self, "Execute:")
      # Change to "inTrade" State
      return "inTrade"
   
   def onExit(self):
      logEvent(self, "Exit   :")

###
#  IN TRADE
###
class InTrade(TradingStrategy.TradingStrategy):
   name = "Basic InTrade"

   def onEnter(self):
      logEvent(self, "Enter  :")
   
   def onExecute(self):
      logEvent(self, "Execute:")
      # Change to "idle" State
      return "idle"
   
   def onExit(self):
      logEvent(self, "Exit   :")