
import csv
import os

PORTFOLIO_FILE = "portfolio_summary.csv"

# Sample current stock prices for demonstration.
# Replace these with actual market prices when needed.
stock_prices = {
    "AAPL": 230.00,
    "GOOGL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "NVDA": 140.00
}

portfolio = {}


def add_stock():
    ticker = input("Enter stock ticker (e.g., AAPL): ").strip().upper()

    if not ticker.isalpha():
        print("Invalid ticker symbol.")
        return

    try:
        buy_price = float(input("Enter purchase price per share: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid price and whole number of shares.")
        return

    if ticker not in stock_prices:
        try:
            current_price = float(
                input("Enter current market price per share: ")
            )
            if current_price <= 0:
                print("Price must be greater than zero.")
                return
            stock_prices[ticker] = current_price
        except ValueError:
            print("Invalid current market price.")
            return

    if ticker in portfolio:
        holding = portfolio[ticker]
        old_quantity = holding["quantity"]
        total_quantity = old_quantity + quantity

        holding["buy_price"] = (
            holding["buy_price"] * old_quantity
            + buy_price * quantity
        ) / total_quantity

        holding["quantity"] = total_quantity

    else:
        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity
        }

    print(f"{ticker} added to your portfolio successfully!")


def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_invested = 0.0
    total_market_value = 0.0

    print("\n" + "=" * 85)
    print("                 STOCK PORTFOLIO SUMMARY")
    print("=" * 85)

    print(
        f"{'Ticker':<10}{'Shares':<10}{'Buy Price':<15}"
        f"{'Current Price':<16}{'Market Value':<16}{'Gain/Loss %':<12}"
    )
    print("-" * 85)

    for ticker, holding in portfolio.items():
        buy_price = holding["buy_price"]
        quantity = holding["quantity"]
        current_price = stock_prices[ticker]

        invested = buy_price * quantity
        market_value = current_price * quantity
        profit_loss = market_value - invested
        percentage = (profit_loss / invested) * 100

        total_invested += invested
        total_market_value += market_value

        print(
            f"{ticker:<10}{quantity:<10}{buy_price:<15.2f}"
            f"{current_price:<16.2f}{market_value:<16.2f}"
            f"{percentage:>+9.2f}%"
        )

    total_profit_loss = total_market_value - total_invested
    overall_percentage = (
        (total_profit_loss / total_invested) * 100
        if total_invested else 0
    )

    print("-" * 85)
    print(f"Total invested:     {total_invested:.2f}")
    print(f"Current market value: {total_market_value:.2f}")
    print(f"Total profit/loss:  {total_profit_loss:+.2f}")
    print(f"Overall return:     {overall_percentage:+.2f}%")


def save_to_csv():
    file_exists = os.path.exists(PORTFOLIO_FILE)

    try:
        with open(PORTFOLIO_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Ticker",
                "Quantity",
                "Buy Price",
                "Current Price",
                "Invested Amount",
                "Market Value",
                "Profit/Loss",
                "Gain/Loss Percentage"
            ])

            for ticker, holding in portfolio.items():
                buy_price = holding["buy_price"]
                quantity = holding["quantity"]
                current_price = stock_prices[ticker]

                invested = buy_price * quantity
                market_value = current_price * quantity
                profit_loss = market_value - invested
                percentage = (profit_loss / invested) * 100

                writer.writerow([
                    ticker,
                    quantity,
                    f"{buy_price:.2f}",
                    f"{current_price:.2f}",
                    f"{invested:.2f}",
                    f"{market_value:.2f}",
                    f"{profit_loss:.2f}",
                    f"{percentage:.2f}"
                ])

        print(f"Portfolio saved to {PORTFOLIO_FILE} successfully!")

    except OSError as error:
        print("Error saving CSV file:", error)


def update_stock_price():
    ticker = input("Enter ticker to update: ").strip().upper()

    if ticker not in portfolio:
        print("Stock not found in your portfolio.")
        return

    try:
        price = float(input("Enter latest market price per share: "))

        if price <= 0:
            print("Price must be greater than zero.")
            return

        stock_prices[ticker] = price
        print(f"Updated {ticker} price to {price:.2f}.")

    except ValueError:
        print("Please enter a valid price.")


def main():
    while True:
        print("\n===== STOCK PORTFOLIO TRACKER =====")
        print("1. Add stock")
        print("2. View portfolio performance")
        print("3. Update current stock price")
        print("4. Save portfolio to CSV")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            update