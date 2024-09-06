import requests
from email import send_email
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define the topic to search for in the news
topic = "medical"

# API key for the News API
api_key = os.getenv("API_KEY")

# Construct the URL for the API request
url = (
    "https://newsapi.org/v2/everything?"
    f"q={topic}&"
    "from=2024-08-10&"
    "sortBy=publishedAt&"
    f"apiKey={api_key}&"
    "language=en"
)

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Initialize the email body with the subject line
body = "Subject: Today's news\n\n"

# Append article titles, descriptions, and URLs to the email body
for article in content["articles"][:10]:
    if article["title"] and article["description"]:
        body += article["title"] + "\n" + article["description"] + "\n" + article.get("url", "") + 2*"\n"

# Encode the body in utf-8
body = body.encode("utf-8")

# Send the email
send_email(message=body)


