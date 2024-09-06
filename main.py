import requests
import os
from email import send_email
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

# Make a request to the News API
request = requests.get(url)

# Get a dictionary with the response data
content = request.json()

# Initialize the email body with the subject line
body = "Subject: Today's news\n\n"

# Append the title, description, and URL of the first 10 articles to the email body
for article in content["articles"][:10]:
    if article["title"] and article["description"]:  # Check if title and description are not None
        body += (
            article["title"] + "\n" +
            article["description"] + "\n" +
            article.get("url", "") + 2 * "\n"
        )

# Encode the email body in utf-8 format
body = body.encode("utf-8")

# Send the email with the news articles
send_email(message=body)
