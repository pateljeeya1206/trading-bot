def validate_order(side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

    if order_type == "LIMIT" and not price:
        raise ValueError("Price required for LIMIT")