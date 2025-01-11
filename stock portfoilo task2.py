import random

class Stock:
    def __init__(self, ticker, quantity):
        self.ticker = ticker
        self.quantity = quantity
        self.purchase_price = self.get_mock_price()  # Use simulated price for purchase
    
    def get_mock_price(self):
        # Simulate getting the stock price using a random number generator
        # You can replace this function with real-time API integration when needed
        return round(random.uniform(50, 500), 2)  # Returns a random price between 50 and 500
    
    def update_price(self):
        # Update the stock price using the simulated price
        self.purchase_price = self.get_mock_price()
        
    def get_value(self):
        # Get the current value of this stock in the portfolio
        return self.get_mock_price() * self.quantity
    
    def get_performance(self):
        # Calculate performance based on price difference from purchase price
        current_price = self.get_mock_price()
        return ((current_price - self.purchase_price) / self.purchase_price) * 100

class Portfolio:
    def __init__(self):
        self.stocks = []
    
    def add_stock(self, ticker, quantity):
        # Add a stock to the portfolio
        new_stock = Stock(ticker, quantity)
        self.stocks.append(new_stock)
        print(f"Added {quantity} shares of {ticker}.")
    
    def remove_stock(self, ticker):
        # Remove a stock from the portfolio
        for stock in self.stocks:
            if stock.ticker == ticker:
                self.stocks.remove(stock)
                print(f"Removed {stock.quantity} shares of {ticker}.")
                return
        print(f"{ticker} not found in the portfolio.")
    
    def display_portfolio(self):
        # Display all stocks in the portfolio
        if not self.stocks:
            print("Your portfolio is empty.")
            return
        print(f"{'Ticker':<10}{'Quantity':<10}{'Current Value':<15}{'Performance (%)'}")
        for stock in self.stocks:
            value = stock.get_value()
            performance = stock.get_performance()
            print(f"{stock.ticker:<10}{stock.quantity:<10}{value:<15.2f}{performance:<15.2f}")
    
    def get_total_value(self):
        # Get the total value of the portfolio
        total_value = sum(stock.get_value() for stock in self.stocks)
        return total_value
    
    def get_total_performance(self):
        # Calculate total portfolio performance
        total_investment = sum(stock.purchase_price * stock.quantity for stock in self.stocks)
        total_value = self.get_total_value()
        return ((total_value - total_investment) / total_investment) * 100

# Main Code
if __name__ == "__main__":
    portfolio = Portfolio()

    # Add stocks to the portfolio
    portfolio.add_stock("AAPL", 10)  # 10 shares of Apple
    portfolio.add_stock("TSLA", 5)   # 5 shares of Tesla

    # Display portfolio details
    portfolio.display_portfolio()

    # Remove stock from portfolio
    portfolio.remove_stock("AAPL")

    # Display updated portfolio details
    portfolio.display_portfolio()

    # Display total portfolio value and performance
    print(f"Total Portfolio Value: ${portfolio.get_total_value():.2f}")
    print(f"Total Portfolio Performance: {portfolio.get_total_performance():.2f}%")
