'''
# FIRST SIMPLE CODE

print("Stock Market Trading Expert System")

price_trend = input("Enter price trend (up/down/stable): ").lower()
volume = input("Enter trading volume (high/low): ").lower()
news = input("Enter market news (positive/negative/neutral): ").lower()

if price_trend == "up" and volume == "high" and news == "positive":
    print("Decision: BUY")
    print("Reason: Stock price is rising with high volume and positive news.")

elif price_trend == "down" and volume == "high" and news == "negative":
    print("Decision: SELL")
    print("Reason: Stock price is falling with high volume and negative news.")

elif price_trend == "stable" or news == "neutral":
    print("Decision: HOLD")
    print("Reason: Market condition is not clear.")

elif price_trend == "down" and volume == "low":
    print("Decision: WAIT")
    print("Reason: Low volume means weak market signal.")

else:
    print("Decision: Analyze More")
    print("Reason: Insufficient information for trading decision.")
'''


def stock_trading_advice(user_input):
    user_input = user_input.lower()

    if "price up" in user_input and "high volume" in user_input and "price" in user_input:
        return "Decision: BUY. Reason: Stock price is increasing with high volume and positive news."

    elif "price down" in user_input and "high volume" in user_input and "negative news" in user_input:
        return "Decision: SELL. Reason: Stock price is falling with high volume and negative news."

    elif "stable" in user_input or "neutral news" in user_input:
        return "Decision: HOLD. Reason: Market condition is stable or unclear."

    elif "price down" in user_input and "low volume" in user_input:
        return "Decision: WAIT. Reason: Low volume shows weak market signal."

    elif "price up" in user_input and "low volume" in user_input:
        return "Decision: WATCH CAREFULLY. Reason: Price is rising but volume support is low."

    elif "negative news" in user_input:
        return "Decision: AVOID BUYING. Reason: Negative news may reduce stock price."

    else:
        return "Decision: Analyze More. Reason: Insufficient market information."


def stock_market_expert_system():
    print("Stock Market Trading Expert System")
    print("Type 'exit' to quit")

    while True:
        market_condition = input("\nEnter stock market condition: ")

        if market_condition.lower() == "exit":
            print("Exiting system. Goodbye!")
            break

        advice = stock_trading_advice(market_condition)
        print("Trading Advice:", advice)


if __name__ == "__main__":
    stock_market_expert_system()