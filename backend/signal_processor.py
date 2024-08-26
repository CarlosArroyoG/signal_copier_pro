import re

class SignalProcessor:
    @staticmethod
    def process_signal(message):
        # Example pattern: BUY EURUSD 1.1200 SL 1.1150 TP 1.1250
        pattern = r"(BUY|SELL)\s+(\w+)\s+([\d.]+)\s+SL\s+([\d.]+)\s+TP\s+([\d.]+)"
        match = re.match(pattern, message)
        
        if match:
            action, symbol, price, sl, tp = match.groups()
            return {
                "action": action,
                "symbol": symbol,
                "price": float(price),
                "sl": float(sl),
                "tp": float(tp)
            }
        return None