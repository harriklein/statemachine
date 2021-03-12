import TradingStrategy
import time

###
#  IDLE 
###
class Idle(TradingStrategy.TradingStrategy):
   name = "Basic Idle"

   def onEnter(self):
      print("\nEnter  :", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )
   
   def onExecute(self):
      print("Execute:", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )
      # Change to "onHold" State
      return "onHold"
   
   def onExit(self):
      print("Exit   :", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )

###
#  ON HOLD
###
class OnHold(TradingStrategy.TradingStrategy):
   name = "Basic OnHold"

   def onEnter(self):
      print("Enter  :", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )
   
   def onExecute(self):
      print("Execute:", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )
      # Change to "inTrade" State
      return "inTrade"
   
   def onExit(self):
      print("Exit   :", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )
###
#  IN TRADE
###
class InTrade(TradingStrategy.TradingStrategy):
   name = "Basic InTrade"

   def onEnter(self):
      print("Enter  :", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )
      self.count = 0
   
   def onExecute(self):
      print("Execute:", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )
      time.sleep(1)
      self.count = self.count + 1
      if self.count < 3: 
         # Force exit but Keep in the current state ("inTrade") 
         return 
      # Change to "idle" State
      return "idle"
   
   def onExit(self):
      print("Exit   :", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )