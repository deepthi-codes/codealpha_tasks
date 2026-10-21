
# Stock Portfolio Tracker
# CodeAlpha Python Programming Internship Project

# Hardcoded stock prices (sample prices in INR)
stock_prices = {
    "AAPL": 225.00,
    "TSLA": 250.00,
    "GOOGL": 180.00,
    "MSFT": 420.00,
    "AMZN": 190.00
}

portfolio = []
total_investment = 0.0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: Rs. {price:.2f}")

# Ask how many stock entries the user wants to add
while True:
    try:
        number_of_stocks = int(
            input("\nHow many stock entries do you want to add? ")
        )
        if number_of_stocks > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Get stock names and quantities
for i in range(number_of_stocks):
    print(f"\nStock entry {i + 1}")

    stock_name = input("Enter stock symbol: ").strip().upper()

    if stock_name not in stock_prices:
        print("Stock not found. This entry will be skipped.")
        continue

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

# Display portfolio summary
print("\n" + "=" * 65)
print("                  YOUR INVESTMENT SUMMARY")
print("=" * 65)

if portfolio:
    print(f"{'Stock':<10}{'Quantity':<12}{'Price (Rs.)':<18}{'Value (Rs.)'}")
    print("-" * 65)

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<12}"
            f"{item['price']:<18.2f}"
            f"{item['investment']:.2f}"
        )

    print("-" * 65)
    print(f"Total Investment: Rs. {total_investment:.2f}")
else:
    print("No valid stock entries were added.")

print("=" * 65)

# Optional: save the report to a text file
if portfolio:
    save_choice = input(
        "\nDo you want to save the report to a text file? (yes/no): "
    ).strip().lower()

    if save_choice in ("yes", "y"):
        try:
            with open("stock_report.txt", "w", encoding="utf-8") as file:
                file.write("STOCK PORTFOLIO TRACKER REPORT\n")
                file.write("=" * 45 + "\n")

                for item in portfolio:
                    file.write(
                        f"Stock: {item['stock']}, "
                        f"Quantity: {item['quantity']}, "
                        f"Price: Rs. {item['price']:.2f}, "
                        f"Value: Rs. {item['investment']:.2f}\n"
                    )

                file.write("-" * 45 + "\n")
                file.write(
                    f"Total Investment: Rs. {total_investment:.2f}\n"
                )

            print("Report saved successfully as stock_report.txt")
        except OSError as error:
            print(f"Could not save the report: {error}")

print("\nThank you for using Stock Portfolio Tracker!")
