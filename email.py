import smtplib
import ssl
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


def send_email(message):
    """
    Sends an email with the provided message using the Gmail SMTP server.

    Args:
        message (str): The message to be sent in the email body.
    """
    # SMTP server details
    host = "smtp.gmail.com"
    port = 465

    # Retrieve email credentials and receiver email from environment variables
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)  # Login to the email server
        server.sendmail(username, receiver, message)  # Send the email
