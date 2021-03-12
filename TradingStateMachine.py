import TradingStrategy
import TradingStrategyBasic

class TradingMachine:
   previousState = None
   currentState  = None
   nextState     = None

   def __init__(self, strategyIdle = None, strategyOnHold = None, strategyInTrade = None):
      if strategyIdle is None:
         self.strategyIdle = TradingStrategy.TradingStrategyNone(self)
      else:
         self.strategyIdle = strategyIdle(self)

      if strategyOnHold is None:
         self.strategyOnHold = TradingStrategy.TradingStrategyNone(self)
      else:
         self.strategyOnHold = strategyOnHold(self)

      if strategyInTrade is None:
         self.strategyInTrade = TradingStrategy.TradingStrategyNone(self)
      else:
         self.strategyInTrade = strategyInTrade(self)

   def run(self, state = "idle"):

      if state not in ["idle", "onHold", "inTrade"]: state = "idle"

      if self.currentState is None:
         self.previousState = state
         self.currentState  = state
         self.nextState     = state

      if   self.currentState == "idle"   : state = self.strategyIdle.onEnter()
      elif self.currentState == "onHold" : state = self.strategyOnHold.onEnter()
      elif self.currentState == "inTrade": state = self.strategyInTrade.onEnter()

      if state not in ["idle", "onHold", "inTrade"]: state = self.currentState

      while self.currentState == self.nextState:
         if   self.currentState == "idle"   : state = self.strategyIdle.onExecute()
         elif self.currentState == "onHold" : state = self.strategyOnHold.onExecute()
         elif self.currentState == "inTrade": state = self.strategyInTrade.onExecute()      
      
         if state not in ["idle", "onHold", "inTrade"]: state = self.currentState

         self.nextState = state

      if   self.currentState == "idle"   : state = self.strategyIdle.onExit()
      elif self.currentState == "onHold" : state = self.strategyOnHold.onExit()
      elif self.currentState == "inTrade": state = self.strategyInTrade.onExit()

      self.previousState = self.currentState
      self.currentState  = self.nextState

      return True




if __name__ == "__main__":
   tradingMachine = TradingMachine(
      TradingStrategyBasic.Idle,
      TradingStrategyBasic.OnHold,
      TradingStrategyBasic.InTrade,
   )
   while tradingMachine.run(): 
      pass
