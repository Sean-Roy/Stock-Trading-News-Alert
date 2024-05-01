import requests
from twilio.rest import Client

# Stock you're interested in:
# TODO: Adjust STOCK_NAME & COMPANY_NAME as desired.
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API & Token information:
# Alpha Vantage: https://www.alphavantage.co/
# TODO: Use your own API keys.
STOCK_API_KEY = "INSERT_YOUR_STOCK_API"
NEWS_API_KEY = "INSERT_YOUR_NEWS_API"

# Twilio: https://www.twilio.com/
# TODO: Use your own numbers & keys/tokens.
VIRTUAL_TWILIO_NUMBER = "+INSERT_YOUR_TWILIO_NUMBER"
VERIFIED_NUMBER = "+INSERT_YOUR_PHONE_NUMBER"  # Your personal phone number
TWILIO_ACCOUNT_SID = "INSERT_YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "INSERT_YOUR_AUTH_TOKEN"

# Get yesterday's closing stock price:
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price:
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Finding the difference between the two:
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Percentage difference:
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# TODO: Set the desired percentage difference.
# If difference percentage is greater than 5%, then get articles:
if abs(diff_percent) > 5:  # ADJ as desired.
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # First 3 articles:
    three_articles = articles[:3]
    print(three_articles)

    # Sending an SMS message for each article's title and description:
    # List of the first 3 articles' title and description:
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}."
                          f"\nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    # Send the messages via Twilio:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
