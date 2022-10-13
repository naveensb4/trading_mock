from maker_taker_base import Maker, Side, Market
from typing import Type


class TrapMaker(Maker):
    def __init__(self) -> None:
        self.trade_list = []
        self.trade_map = {Side.buy:
                          {"market": Market(15, 1, 25, 1),
                           Side.buy: Market(50, 1, 60, 1),
                           Side.sell: Market(10, 1e9, 20, 1e9)},
                          Side.sell:
                          {"market": Market(0, 1e9, 10, 1e9),
                           Side.buy: Market(2.5, 1e9, 12.5, 1e9),
                           Side.sell: Market(-2.5, 1e9, 7.5, 1e9)}}

    def update_trade(self, side: Type[Side]) -> None:
        self.trade_list.append(side)

    def get_market(self, round: int) -> Market():
        if len(self.trade_list) == 1:
            return self.trade_map[self.trade_list[0]]["market"]
        if len(self.trade_list) == 2:
            return self.trade_map[self.trade_list[0]][self.trade_list[1]]
        return Market(5, 1, 15, 1)
