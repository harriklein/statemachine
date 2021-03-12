import signal
import TradingStrategy
import TradingStrategyBasic

class TradingStateMachine:
   stopped       = False
   previousState = None
   currentState  = None
   nextState     = None

   ### Initialize the Trading Machine with given Strategies
   def __init__(self, strategyIdle = None, strategyOnHold = None, strategyInTrade = None):
      self.stopped = False
      if strategyIdle    is None: self.strategyIdle    = TradingStrategy.TradingStrategyNone(self)
      else                      : self.strategyIdle    = strategyIdle(self)

      if strategyOnHold  is None: self.strategyOnHold  = TradingStrategy.TradingStrategyNone(self)
      else                      : self.strategyOnHold  = strategyOnHold(self)

      if strategyInTrade is None: self.strategyInTrade = TradingStrategy.TradingStrategyNone(self)
      else                      : self.strategyInTrade = strategyInTrade(self)

   ### 
   def run(self, state = "idle"):

      # Validate State
      if state not in ["idle", "onHold", "inTrade"]: state = "idle"

      # initialize on the first time. Default = 'idle'
      if self.currentState is None:
         self.previousState = state
         self.currentState  = state
         self.nextState     = state

      # call onEnter
      if   self.currentState == "idle"   : state = self.strategyIdle.onEnter()
      elif self.currentState == "onHold" : state = self.strategyOnHold.onEnter()
      elif self.currentState == "inTrade": state = self.strategyInTrade.onEnter()

      # Validate return of onEnter
      if state not in ["idle", "onHold", "inTrade"]: state = self.currentState

      # Loop while it doesn't change the state
      while (self.currentState == self.nextState) and (not self.stopped):
         # call onExecute
         if   self.currentState == "idle"   : state = self.strategyIdle.onExecute()
         elif self.currentState == "onHold" : state = self.strategyOnHold.onExecute()
         elif self.currentState == "inTrade": state = self.strategyInTrade.onExecute()      

         # Validate return and change state if requested       
         if state not in ["idle", "onHold", "inTrade"]: state = self.currentState
         self.nextState = state

      # onExit
      if   self.currentState == "idle"   : state = self.strategyIdle.onExit()
      elif self.currentState == "onHold" : state = self.strategyOnHold.onExit()
      elif self.currentState == "inTrade": state = self.strategyInTrade.onExit()

      # Update states
      self.previousState = self.currentState
      self.currentState  = self.nextState

      return not self.stopped

   # Graceful stop
   def stop(self, signal, frame):
      self.stopped = True


###
if __name__ == "__main__":
   tradingMachine = TradingStateMachine(
      TradingStrategyBasic.Idle,
      TradingStrategyBasic.OnHold,
      TradingStrategyBasic.InTrade,
   )
   signal.signal(signal.SIGINT , tradingMachine.stop)
   signal.signal(signal.SIGTERM, tradingMachine.stop)
   while tradingMachine.run(): 
      pass
