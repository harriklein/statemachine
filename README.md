# statemachine


Basic of State Machine with option to change strategy

Each state is inherited from TradingStrategy class, which implements 3 events: onEnter, onExecute, onExit

```python
class TradingStrategy:
   name = ""
   stateMachine = None

   def __init__(self, stateMachine = None):
      self.stateMachine = stateMachine

   # Events
   #   return: Next State. Default: Keep same State 
   def onEnter(self): pass
   def onExecute(self): pass
   def onExit(self): pass
```

Into each TradingStrategy class events, you can access the previousState, currentState and nextState trough the variable stateMachine.


The state machine implements 3 states ("idle", "onHold" and "inTrade") and you can specify a custom TradingStrategy class when create the StateMachine.
To change the state you just need to return the state on the events. e.g.:

```python
   def onEnter(self):
      print("\nEnter  :", self.name, "\t", 
         "\tprv:", self.stateMachine.previousState, 
         "\tcur:", self.stateMachine.currentState, 
         "\tnxt:", self.stateMachine.nextState
      )       
      # Yes, it's possible to change the state on the onEnter event. 
      # It avoids onExecute event, but triggers onExit event.
      return "onHold"
   
   def onExecute(self):
      return "idle"
```

To run the StateMachine, use the method run(), which you can define the initial state as parameter ("idle" by default)
The state machine implements a loop on the event onExecute until you change to a new state 

```python
   tradingMachine = TradingStateMachine(
      TradingStrategyBasic.Idle,
      TradingStrategyBasic.OnHold,
      TradingStrategyBasic.InTrade,
   )
   while tradingMachine.run(): 
      pass
```

In the example above, we create a new state machine with a basic strategy loop among the 3 states.

```python
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
```

output:
```
Enter  : Basic Idle             prv: idle       cur: idle       nxt: idle
Execute: Basic Idle             prv: idle       cur: idle       nxt: idle
Exit   : Basic Idle             prv: idle       cur: idle       nxt: onHold
Enter  : Basic OnHold           prv: idle       cur: onHold     nxt: onHold
Execute: Basic OnHold           prv: idle       cur: onHold     nxt: onHold
Exit   : Basic OnHold           prv: idle       cur: onHold     nxt: inTrade
Enter  : Basic InTrade          prv: onHold     cur: inTrade    nxt: inTrade
Execute: Basic InTrade          prv: onHold     cur: inTrade    nxt: inTrade
Execute: Basic InTrade          prv: onHold     cur: inTrade    nxt: inTrade
Execute: Basic InTrade          prv: onHold     cur: inTrade    nxt: inTrade
Exit   : Basic InTrade          prv: onHold     cur: inTrade    nxt: idle
```

