import requests
from twilio.rest import Client

# API endpoint and query parameters
url = "https://famous-quotes4.p.rapidapi.com/random"
querystring = {"category": "all", "count": "1"}

# Add your RapidAPI key here
headers = {
    "x-rapidapi-key": "your_rapidapi_key", # <--- Add your rapid api key here
    "x-rapidapi-host": "famous-quotes4.p.rapidapi.com"
}

def get_quote():
    try:
        # Send the GET request
        response = requests.get(url, headers=headers, params=querystring)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        quotes = response.json()

        # Check if quotes is a list and contains data
        if isinstance(quotes, list) and quotes:
            # Extract information from the first quote
            text = quotes[0].get('text', 'No text available')
            author = quotes[0].get('author', 'Unknown author')
            return f"{text} - {author}"
        else:
            return "No quote found - Unknown author"

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the quote: {e}")
        return "Failed to retrieve quote - Unknown author"

def send_sms(msg):
    # Add your Twilio account SID and auth token here
    account_sid = "your_account_sid" # <--- Add your twilio account sid here
    auth_token = "your_auth_token" # <--- Add your twillio account auth token here

    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Send the message using Twilio
        message = client.messages.create(
            from_='+your_twilio_number', # <--- Replace with your Twilio phone number
            body=msg,
            to='+your_phone_number'     # <--- Replace with your phone number
        )

        # Print the message SID to confirm successful sending
        print("Message SID:", message.sid)

    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

if __name__ == "__main__":
    # Get the quote
    quote_message = get_quote()
    
    # Send the quote via SMS
    send_sms(quote_message)
