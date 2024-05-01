# Stock-Trading-News-Alert
A comprehensive program that checks for specific stock's price changes and sends the top 3 news headlines related to the company directly to your phone as an SMS, utilizing API calls and more.

User is required to acquire and utilize their own API and secret keys, as well as a virtual number from Twilio and their own personal number.

Key information required are the below:
* STOCK_NAME: This is the desired ticker symbol.
* COMPANY_NAME: This is the company name associated with the ticker.
* STOCK_API_KEY: This can be acquired from https://www.alphavantage.co/ using your own account.
* NEWS_API_KEY: This can be acquired from https://www.alphavantage.co/ using your own account.
* VIRTUAL_TWILIO_NUMBER: This is your virtual Twilio number. This can be acquired from https://www.twilio.com/ using your own account.
* VERIFIED_NUMBER: This is your own personal phone number where the SMS will be sent.
* TWILIO_ACCOUNT_SID: This can be acquired from https://www.twilio.com/ using your own account.
* TWILIO_AUTH_TOKEN: This can be acquired from https://www.twilio.com/ using your own account.
* In the line where it reads "ADJ as desired.", change the number to your desired percentage difference.
