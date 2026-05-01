# cli.py
import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(args.side, args.type, args.quantity, args.price)

        client = get_client()

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ ORDER SUCCESS")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

    except Exception as e:
        print("\n❌ ORDER FAILED")
        print(str(e))

if __name__ == "__main__":
    main()