from maker_taker_base import Maker, Market

class NaveenMaker(Maker):
    def __init__(self):
        self.fair_value = 50 #initial value of contract
        self.price_range = 10
                      
    def get_market(self, round: int) -> Market:
      spread = 10 if round < 10 else 5  # Decreasing spread over rounds
      return Market(self.value - spread, 1, self.value + spread, 1)

    def update_trade(self, side: Type[Side]):
      # If the trade was successful, adjust the value of the contract
      if side == Side.buy:
          self.value += 5
      elif side == Side.sell:
          self.value -= 5
        
#The above code defines a Maker class named NaveenMaker that aims to profit against Greedy Taker. 
#The class has an initial value for the contract of 50, which can be adjusted over time based on the trades that are made. 
#The get_market method returns the bid and ask prices for the contract, with a spread that decreases over time. 
#The update_trade method adjusts the value of the contract based on the outcome of each trade.
