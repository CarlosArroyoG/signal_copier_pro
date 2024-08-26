import MetaTrader5 as mt5

class MT5Connector:
    @staticmethod
    def initialize(login, password, server):
        if not mt5.initialize(login=login, password=password, server=server):
            print("MT5 initialization failed")
            return False
        return True

    @staticmethod
    def shutdown():
        mt5.shutdown()

    @staticmethod
    def place_order(symbol, order_type, volume, price, sl, tp):
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "magic": 234000,
            "comment": "python script",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        return result