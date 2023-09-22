import os
from twilio.rest import Client
import smtplib
import requests

SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT_2")
SHEETY_API_AUTH = os.environ.get("SHEETY_API_AUTH")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
FROM_PHONE = os.environ.get("FROM_PHONE")
TO_PHONE = os.environ.get("TO_PHONE")
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message):
        self.message = message
        self.send_text()
        self.send_email()

    def send_text(self):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=self.message,
            from_=FROM_PHONE,
            to=TO_PHONE
        )
        print(message.status)

    def send_email(self):
        headers = {
            "Authorization": SHEETY_API_AUTH
        }

        users_data = requests.get(url=SHEETY_API_ENDPOINT, headers=headers)
        users_data.raise_for_status()

        users = users_data.json()["users"]
        emails = []
        for user in users:
            emails.append(user["email"])
        print(f"sending to: {emails}")
        for email in emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=self.message)
