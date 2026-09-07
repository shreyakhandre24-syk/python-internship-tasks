#  Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 200
}

total_investment = 0

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

while True:

    stock_name = input("Enter stock name (or 'done' to finish): ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print("Stock:", stock_name)
        print("Price:", stock_prices[stock_name])
        print("Quantity:", quantity)
        print("Investment:", investment)

    else:
        print("Stock not available. Please try again.")

print("=" * 40)
print("Total Investment:", total_investment)
print("=" * 40)