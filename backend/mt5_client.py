import MetaTrader5 as mt5
import subprocess
import time
import os

class MT5Client:
    DERIV5_PATH = os.getenv('DERIV5_PATH', 'C:\\Program Files\\Deriv\\Deriv 5\\terminal64.exe')

    @staticmethod
    def initialize(login, password, server):
        if not mt5.initialize():
            print("MT5 not initialized. Attempting to start Deriv5...")
            subprocess.Popen([MT5Client.DERIV5_PATH])
            time.sleep(10)  # Espera a que Deriv5 se inicie
            if not mt5.initialize():
                print("Deriv5 initialization failed")
                return False

        if not mt5.login(login, password, server):
            print(f"Login failed for account {login}")
            return False
        
        print("MT5 initialized and logged in successfully")
        return True

    @staticmethod
    def shutdown():
        mt5.shutdown()

    @staticmethod
    def place_order(symbol, order_type, volume, price, sl, tp):
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": float(volume),
            "type": order_type,
            "price": float(price),
            "sl": float(sl) if sl else None,
            "tp": float(tp) if tp else None,
            "magic": 234000,
            "comment": "python script",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        return result

    @staticmethod
    def get_account_info():
        return mt5.account_info()

    @staticmethod
    def get_positions():
        return mt5.positions_get()
