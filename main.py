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

# Access the article titles and description
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
# print(body)

